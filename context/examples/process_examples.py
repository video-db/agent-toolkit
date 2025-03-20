import os
import glob
import fnmatch

import urllib.parse
import nbformat
from nbconvert import MarkdownExporter
import yaml

import context.utils as utils  # Your custom LLM utilities


def format_url(url: str) -> str:
    return urllib.parse.quote(url, safe=":/?=&")


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


class IPYNBHandler:
    """
    Handles the conversion and processing of Jupyter Notebook (.ipynb) files.
    """

    def __init__(
        self,
        include_patterns,
        exclude_patterns,
        prompt_config,
        clone_dir,
        clone_url,
        llm,
    ):
        self.include_patterns = include_patterns
        self.exclude_patterns = exclude_patterns
        self.prompt_config = prompt_config
        self.clone_dir = clone_dir
        self.clone_url = clone_url
        self.llm = llm

    def convert_ipynb_to_md(self, ipynb_file):
        """
        Convert a Jupyter Notebook to Markdown using nbconvert.
        """
        with open(ipynb_file, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)
        exporter = MarkdownExporter()
        md_content, _ = exporter.from_notebook_node(notebook)
        return md_content

    def get_prompt_for_ipynb(self, file_path):
        """
        Determine which prompt to use based on the file path and prompt configuration.
        """
        default_prompt = self.prompt_config.get("default_prompt", "")
        prompt_folder = self.prompt_config.get("prompt_folder", "")
        custom_prompts = self.prompt_config.get("custom_prompts", [])
        selected_prompt = default_prompt

        for entry in custom_prompts:
            pattern = entry.get("pattern")
            prompt_file = entry.get("prompt")
            if pattern and prompt_file:
                # Last matching prompt wins
                if fnmatch.fnmatch(file_path, f"{self.clone_dir}/{pattern}"):
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

    def get_ipynb_files_from_globs(self):
        """
        Expand include glob patterns into a list of .ipynb file paths
        and filter out files matching any exclude pattern.
        """
        files = []
        for pattern in self.include_patterns:
            matched = glob.glob(f"{self.clone_dir}/{pattern}", recursive=True)
            files.extend(matched)
        if self.exclude_patterns:
            filtered_files = []
            for f in files:
                if any(
                    fnmatch.fnmatch(f, f"{self.clone_dir}/{pat}")
                    for pat in self.exclude_patterns
                ):
                    continue
                filtered_files.append(f)
            files = filtered_files
        return files

    def process(self):
        """
        Process each .ipynb file:
          - Convert to Markdown.
          - Simplify content via the LLM.
          - Append the result to a combined Markdown string.

        Returns:
            str: The combined Markdown content.
        """
        ipynb_files = self.get_ipynb_files_from_globs()
        combined_content = ""

        for ipynb_file in ipynb_files:
            if not os.path.exists(ipynb_file):
                print(f"⚠ File not found: {ipynb_file}")
                continue

            print(f"Processing {ipynb_file}...")

            # Convert notebook to Markdown
            md_content = self.convert_ipynb_to_md(ipynb_file)
            prompt_text = self.get_prompt_for_ipynb(ipynb_file)
            simplified_content, tokens_used = simplify_content_with_llm(
                prompt_text, md_content, self.llm
            )
            file_title = os.path.basename(ipynb_file).replace(".ipynb", "")
            print(f"💰 Tokens Used {tokens_used}")
            source_link = ipynb_file.replace(
                self.clone_dir, f"{self.clone_url}/blob/main"
            )
            combined_content += (
                f"# IPYNB Notebook: {file_title} [Source Link]({format_url(source_link)})\n\n"
                + simplified_content
                + "\n\n---\n\n"
            )

        prompt_folder = self.prompt_config.get("prompt_folder", "")
        refined_prompt_file = self.prompt_config.get("fine_refinment_prompt", "")
        refined_prompt_path = os.path.join(prompt_folder, refined_prompt_file)
        with open(refined_prompt_path, "r", encoding="utf-8") as f:
            refined_prompt = f.read()
        refined_content = simplify_content_with_llm(refined_prompt, combined_content)
        return refined_content


if __name__ == "__main__":
    # Load configuration from YAML
    config = load_config_yaml().get("examples_context", {})
    clone_dir = config.get("clone_dir")
    clone_url = config.get("clone_url")

    # Retrieve the LLM parameter from the config; default to "gemini" if not provided.
    llm = config.get("llm", "gemini")

    # IPYNB configuration
    ipynb_include = config.get("include", [])
    ipynb_exclude = config.get("exclude", [])
    ipynb_prompts = config.get("prompts", {})
    ipynb_output_file = config.get("output_file", "")

    final_output_file = config.get("output_file", "")

    # Process IPYNB files
    ipynb_handler = IPYNBHandler(
        ipynb_include, ipynb_exclude, ipynb_prompts, clone_dir, clone_url, llm
    )
    ipynb_content = ipynb_handler.process()

    # Save IPYNB content to the desired output file
    if ipynb_output_file:
        os.makedirs(os.path.dirname(ipynb_output_file), exist_ok=True)
        with open(ipynb_output_file, "w", encoding="utf-8") as f:
            f.write(ipynb_content)
        print(f"✔ IPYNB content saved in {ipynb_output_file}")
