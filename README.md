![Latest Number](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/video-db/agent-toolkit/refs/heads/main/readme_shields.json&style=for-the-badge)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/video-db/agent-toolkit?style=for-the-badge)
![stars-shield](https://img.shields.io/github/stars/video-db/agent-toolkit.svg?style=for-the-badge)
![issues-shield](https://img.shields.io/github/issues/video-db/agent-toolkit.svg?style=for-the-badge)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://videodb.io/">
    <img src="https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-RgjcFrrJjj/d3cbc44f8584ecd42f2a97d981a144dce6a66d83ddd5864f723b7808c7d1dfbc25034f2f25e1b2188e78f78f37bcb79d3c34ca937cbb08ca8b3da1526c29da9a897ab38eb39d084fd715028b7cc60eb595c68ecfa6fa0bb125ec2b09da65664a4f172c2f" alt="Logo" width="300" height="">
  </a>

  <h3 align="center">VideoDB Agent Toolkit</h3>

  <p align="center">
    AI Agent toolkit for VideoDB
    <br />
    <a href="https://videodb.io/llms.txt"><strong>llms.txt »</strong></a> <br/>
    <a href="https://videodb.io/llms-full.txt"><strong>llms-full.txt »</strong></a>
    <br />
  </p>
</p>

# Agent Toolkit for VideoDB

This repository provides tools and context files to help integrate VideoDB into AI applications, LLM-powered agents, and coding tools such as AI Coding IDEs.

## 📦 Components

### 1. llms-full.txt
---

A consolidated reference file that provides:
- Background information on VideoDB
- SDK usage and interface documentation
- Sample usage from VideoDB Docs and Cookbook
- Integration guidance for LLM-based environments

This file is designed to be injected as context into LLMs, AI agents, and smart developer tools to enable better understanding and usage of VideoDB in real time.

[llms-full.txt](https://videodb.io/llms-full.txt) can be found at https://videodb.io/llms-full.txt


### 2. llms.txt
---

A leaner, standards-compliant file designed for use with LLMs at inference time.
It follows the [llms.txt proposal by Answer.AI](https://github.com/answerdotai/llms-txt), which outlines how to provide LLM-readable metadata and API context about a website or tool.

> Use llms.txt for LLM discoverability and llms-full.txt for deep contextual understanding in IDEs and agents.

[llms.txt](https://videodb.io/llms.txt) can be found at https://videodb.io/llms.txt

### 3. MCP (Model Context Protocol)
---

More on MCP usage coming soon.




## 🧠 What is a “LLM Context File”?

LLM Context Files are documents designed to optimize how large language models interact with external tools and SDKs. They can be injected at runtime into agents, copilots, or IDE assistants to give them deep knowledge of a product or API.

VideoDB’s Context Files Include:
- Usage instructions and tips
- SDK structure and interface definitions
- Compiled documentation and examples
- Cookbook patterns for solving common use cases

`llms-full.txt` is composed of several core content blocks — here’s how they stack up.
![](./token_breakdown.png)

## ⚙️ How is the LLM Context File Generated?

The `llms-full.txt` file is automatically generated from a set of core building blocks, including:

- VideoDB SDK source files  
- Official VideoDB documentation  
- Curated examples from the [VideoDB Cookbook](https://github.com/video-db/videodb-cookbook)  
- Agent-specific usage instructions and patterns

To ensure the context file remains up-to-date and in sync with the evolving SDK and docs, we use a set of GitHub Actions that automatically regenerate and publish `llms-full.txt` whenever any of the source components are updated.

For example:
- Adding a new function to the SDK triggers an update to the SDK section  
- Updating a cookbook example refreshes the relevant usage context  
- Changes to docs are recompiled into the Docs Context block

This automation ensures that LLMs and AI tools always receive the most accurate and complete information — without requiring manual intervention.

### 1. Update SDK Context

**Trigger:**  
- **Manual:** Triggered via `workflow_dispatch`.
- **Event-based:** Triggered by a `repository_dispatch` event of type `sdk-context-update`.

**Workflow:**  
- **Clone & Build:** The workflow clones the SDK repository, sets up a Python environment, and builds the documentation using Sphinx.
- **Commit:** It pulls the latest changes from the main branch, commits the generated documentation to a new branch, and pushes the branch.
- **Pull Request:** Finally, a pull request is created to merge the updated documentation into the main branch.

**Configuration:**  : 
> Config path: `config.yaml/sdk_context`
  - **clone_url:** The URL of the SDK repository to clone (e.g., `https://github.com/video-db/videodb-python`).
  - **clone_dir:** The local directory where the SDK repository will be cloned (e.g., `context/sdk/source`).
  - **sphinx_config_dir:** The directory containing the Sphinx configuration (e.g., `context/sdk/sphinx_config`).
  - **output_dir:** The directory where Sphinx generates the documentation output (e.g., `context/sdk/context`).
  - **commit_message:** The commit message used when committing the generated Sphinx Markdown output.
  - **branch_name:** The branch name to which the changes are pushed (e.g., `sdk-context-branch`).


### 2. Update Docs Context

**Trigger:**  
- **Manual:** Triggered via `workflow_dispatch`.

**Workflow:**  
- **Scrape:** The workflow scrapes the [documentation site](https://docs.videodb.io) to generate a doc tree JSON.
- **Filtering:**  
  The workflow uses the `include` and `exclude` patterns from the configuration to determine which documents should be processed  only the relevant documentation is selected.(it uses doc tree JSON to see hierarchical strucutue)
- **Crawling:**  
  Each selected document is then crawled using [FireCrawl](https://www.firecrawl.dev/) to retrieve its content. The crawler converts the fetched content into a Markdown format.
- **LLM Processing:**  
  The Markdown output of each document is processed through an LLM for summarization and refinement. The prompt used by the LLM is configurable through the prompts settings in the configuration file using `prompts` key, allowing for customized processing of each document.

- **Consolidation:**  
  Finally, all LLM-processed Markdown outputs are consolidated into a single file and saved as the final documentation context output.
- **Commit:** Finally, it commits and pushes the changes (or opens a pull request) to update the docs context in the repository.

**Configuration:**  
> Config path: `config.yaml/docs_context.doc_tree_scrape_config`
  - **script:** The crawler script (e.g., `context/docs/crawl_coda_tree.py`).
  - **output:** The JSON file path where the scraped doc tree is stored (e.g., `context/docs/doc_tree.json`).
  - **url, selector, selector_value:** Parameters used to scrape the documentation site (e.g., `https://docs.videodb.io` and corresponding HTML attributes).

> Config Path: `config.yaml/docs_context`
  - **include** & **exclude**: A list of glob-like patterns that determine which  pages from the scraped documentation tree should be included & excluded in the final output.   

    > Example: This config will include all pages & subpages under [Welcome to Videodb Docs](https://docs.videodb.io/), [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38), [Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80) except [Quickstart Guide/Collections](https://docs.videodb.io/collections-68)
    ```yaml
    include:
      - "Welcome to Videodb Docs"
      - "Quick Start Guide/*"
      - "Visual Search and Indexing/*"
    exclude:
      - "Quick Start Guide/Collections"

    ```
  - **prompts**: This section has config for how the content should be refined using an LLM during the processing phase.
    - **prompt_folder**: The path to folder which has prompt
    - **default_folder**: The file name of the default prompt should be used in llm processing part for the documents 
    - **custom_prompt**: A list with keys `pattern` and `prompt`, which specifies overriding prompt for a file or pattern

    > Example: This configuration ensures that, while most of the documentation will be processed using the default prompt, any pages under [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38) will be refined using a specialized prompt that may better suit their content and structure
    ```yaml
    prompts:
      prompt_folder: "context/prompts"         # Directory where all prompt files are stored.
      default_prompt: "default_docs.txt"         # Default prompt file used for most pages.
      custom_prompts:
        - pattern: "Quick Start Guide/*"         # Matches all pages under "Quick Start Guide".
          prompt: "custom_quickstart.txt"         # Uses this custom prompt instead of the default.
    ```

  -  **base_url**: The base URL for the documentation site. This is used to resolve any relative links that are found during scraping.
  - **tree_file**: Specifies the location of the JSON file that stores the scraped documentation tree. This file is generated by the crawler and later used to filter and process the content.
  - **output_file**: The path where the consolidated Markdown output for the docs context will be written. This file will contain the final, merged documentation content.
  - **script_path**: The path to the processing script that converts the scraped doc tree (and other docs data) into a consolidated Markdown file
  - **branch_name** : The name of the branch that will be used when committing and pushing the updated docs context. This allows the update to be reviewed via a pull request before merging.
  - **commit_message**: The commit message used when updating the docs context. This message describes the changes made by the workflow.
  - **llm**: Specifies which Language Model (LLM) is used to process and refine the scraped documentation content. This setting ensures that the appropriate model (e.g., “gemini”) is used during the summarization or cleanup stages.

---



### 💡 Why Use This Toolkit?
---
- 🔍 Improve VideoDB Code suggestions in AI coding environments
- 🧠 Give agents real-time awareness of VideoDB’s capabilities
- 📚 Provide LLMs with instant access to relevant SDK context
- 🚀 Enable smooth integration of VideoDB into any AI-powered application


### 📌 Coming Soon
---
- Expanded MCP examples and plugin support
- Integration templates for VSCode, Cursor, Continue.dev
- Recipes for deploying VideoDB with LangChain, LlamaIndex, and more