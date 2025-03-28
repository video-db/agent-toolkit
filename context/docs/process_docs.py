import os
import fnmatch
import json

import yaml

from firecrawl import FirecrawlApp
import context.utils as utils  # Your custom LLM utilities


def simplify_content_with_llm(prompt_text, text, llm):
    """
    Simplify Markdown content using an LLM.

    Parameters:
        prompt_text (str): The prompt to guide the simplification.
        text (str): The original Markdown content.
        llm (str): The language model identifier to use.

    Returns:
        str: The simplified Markdown content.
    """
    if not prompt_text:
        prompt_text = """
        Simplify the following Markdown content.
        Remove fluff and keep only key technical details.
        Remove any extraneous buttons or sections.
        """
    llm_output = utils.get_llm_output(prompt_text, text, llm=llm)
    return llm_output["response"], llm_output["usage"]


def load_config_yaml():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class DocsHandler:
    """
    Handles the processing of documentation files.
    """

    def __init__(
        self,
        include_patterns,
        exclude_patterns,
        prompt_config,
        base_url,
        doc_tree_file,
        docs_output_fragments,
        llm,
    ):
        self.include_patterns = include_patterns
        self.exclude_patterns = exclude_patterns
        self.prompt_config = prompt_config
        self.base_url = base_url
        self.doc_tree_file = doc_tree_file
        self.docs_output_fragments = docs_output_fragments
        self.llm = llm

    def traverse_doc_tree(self, doc_tree, parent_path=""):
        """
        Traverse a documentation tree structure and return a list of tuples (full_path, href, element).
        """
        results = []
        for node in doc_tree:
            current = (
                os.path.join(parent_path, node["element"])
                if parent_path
                else node["element"]
            )
            results.append((current, node.get("href", ""), node["element"]))
            if node.get("children"):
                results.extend(self.traverse_doc_tree(node["children"], current))
        return results

    def scrape_document_to_md(self, url):
        """
        Scrape a document URL and return its Markdown content.
        """
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise Exception("FirewCrawl API Key missing")
        app = FirecrawlApp(api_key=api_key)
        response = app.scrape_url(url=url, params={"formats": ["markdown"]}).get(
            "markdown", ""
        )
        return response

    def get_prompt_for_identifier(self, identifier):
        """
        Determine which prompt to use based on the document identifier and prompt configuration.
        """
        prompt_folder = self.prompt_config.get("prompt_folder", "")
        default_prompt = self.prompt_config.get("default_prompt", "")
        custom_prompts = self.prompt_config.get("custom_prompts", [])
        selected_prompt = default_prompt

        for entry in custom_prompts:
            pattern = entry.get("pattern")
            prompt_file = entry.get("prompt")
            if pattern and prompt_file and fnmatch.fnmatch(identifier, pattern):
                selected_prompt = prompt_file

        full_prompt_path = os.path.join(prompt_folder, selected_prompt)
        if os.path.exists(full_prompt_path):
            with open(full_prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            print(
                f"Warning: Prompt file {full_prompt_path} not found. Using empty prompt."
            )
            return ""

    def process(self):
        """
        Process the documentation tree:
          - Traverse the doc tree to identify docs to include.
          - Scrape each doc URL.
          - Simplify its Markdown content via the LLM.
          - Append the result to a combined Markdown string.

        Returns:
            str: The combined Markdown content.
        """
        with open(self.doc_tree_file, "r", encoding="utf-8") as f:
            doc_tree = json.load(f)

        docs = self.traverse_doc_tree(doc_tree)
        selected = []
        for full_path, href, element in docs:
            include = True
            if self.include_patterns:
                include = any(
                    fnmatch.fnmatch(full_path, pat) for pat in self.include_patterns
                )
            exclude = False
            if self.exclude_patterns:
                exclude = any(
                    fnmatch.fnmatch(full_path, pat) for pat in self.exclude_patterns
                )
            if include and not exclude:
                selected.append((full_path, href, element))

        output = ""
        total_tokens_used = 0
        for full_path, href, element in selected:
            # Build full URL based on the href value.
            url = self.base_url.rstrip("/") + href if href.startswith("/") else href
            try:
                content = self.scrape_document_to_md(url)
            except Exception as e:
                content = f"Error fetching {url}: {str(e)}"
            prompt_text = self.get_prompt_for_identifier(full_path)
            simplified, tokens_used = simplify_content_with_llm(
                prompt_text, content, self.llm
            )
            print(f"💰 Tokens Used {tokens_used}")
            total_tokens_used += tokens_used
            doc_output = (
                f"# {element} [Source Link]({self.base_url}{href})\n\n"
                + simplified
                + "\n\n---\n\n"
            )
            if self.docs_output_fragments:
                os.makedirs(os.path.dirname(self.docs_output_fragments), exist_ok=True)
                doc_output_file = os.path.join(
                    self.docs_output_fragments,
                    f"{href.replace('-', '_').trim('/')}.txt",
                )
                with open(doc_output_file, "w") as f:
                    f.write(doc_output)
            output += doc_output
        print(f"💰 💰 Total Tokens Used : {total_tokens_used}")
        return output


if __name__ == "__main__":
    # Load configuration from YAML
    config = load_config_yaml().get("docs_context", {})
    clone_dir = config.get("clone_dir")

    # Retrieve the LLM parameter from the config; default to "gemini" if not provided.
    llm = config.get("llm", "gemini")

    # Docs configuration
    docs_include = config.get("include", [])
    docs_exclude = config.get("exclude", [])
    docs_prompts = config.get("prompts", {})
    docs_output_fragments = config.get("output_fragments")
    docs_output_file = config.get("output_file", "")
    docs_base_url = config.get("base_url", "")
    docs_tree_file = config.get("tree_file", "")

    # Process Docs
    docs_handler = DocsHandler(
        docs_include,
        docs_exclude,
        docs_prompts,
        docs_base_url,
        docs_tree_file,
        docs_output_fragments,
        llm,
    )
    docs_content = docs_handler.process()

    # Save Docs content to the desired output file
    if docs_output_file:
        os.makedirs(os.path.dirname(docs_output_file), exist_ok=True)
        with open(docs_output_file, "w", encoding="utf-8") as f:
            f.write(docs_content)
        print(f"✔ Docs content saved in {docs_output_file}")
