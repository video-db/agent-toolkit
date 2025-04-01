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

# VideoDB Agent Toolkit

This repository provides comprehensive tools and context files for integrating VideoDB into AI applications, LLM-powered agents, and AI coding IDEs.

## 📦 Toolkit Components

### 1. llms-full.txt ([View »](https://videodb.io/llms-full.txt))
---
A complete reference providing:

- Detailed VideoDB background
- SDK usage and documentation
- Integration guidance and practical examples

Designed for deep contextual understanding and real-time injection into IDEs and agents.




### 2. llms.txt ([View »](https://videodb.io/llms.txt))

A streamlined, standards-compliant file following the [Answer.AI llms.txt proposal](https://github.com/answerdotai/llms-txt) for discoverability and metadata exposure to LLMs during inference.

> **ℹ️ Recommendation**: Use llms.txt for basic discovery and llms-full.txt for comprehensive integration.


### 3. 🚧 MCP (Model Context Protocol)

👷 Under active development. Documentation coming soon.


## 🧠 What's in an LLM Context File?

VideoDB’s context files include:
- Usage instructions and tips
- SDK structure and interface definitions
- Compiled documentation and examples
- Cookbook patterns for solving common use cases

Here’s how `llms-full.txt` stack up.
![](./token_breakdown.png)

Files are automatically maintained to stay current with SDK, documentation, and examples updates.

## 🤖 Automated Context Generation and Updates

Automated context generation ensures context files remain accurate and up-to-date by immediately reflecting changes from their source repositories.   

For example, adding or updating a function in the SDK automatically triggers updates to the corresponding SDK context, ensuring LLMs and agents always work with the latest information.

Automation is achieved through GitHub Actions, configured centrally via [config.yaml](https://github.com/video-db/agent-toolkit/blob/main/config.yaml)

### 📌 SDK Context Updates
---

[View Github Workflow File »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_sdk_context.yml)

This Github Workflow automates the process of building and updating the SDK Context Part in LLM Context. 

#### Trigger:  
- **Manual:** Triggered via `workflow_dispatch`.
- **Event-based:** Triggered by a `repository_dispatch` event of type `sdk-context-update`.

#### Workflow:  

- **Clone:** Clones the latest version of the [SDK repository](https://github.com/video-db/videodb-python)

- **Build Documentation:** Uses [Sphinx](https://www.sphinx-doc.org/en/master), a documentation generator, to parse Python docstrings from SDK source code

- **Commit & PR** : Commits the generated documentation into a dedicated branch and creates a pull request to review and merge updates

### 📌 Documentation Context Updates
---

[View Github Workflow File »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_docs_context.yml)

This workflow automates the update of the documentation context in llm context by scraping and processing the documentation site. 

#### Trigger:  
- **Manual:** Triggered via `workflow_dispatch`.

#### Workflow:  
- **Scrape:** The workflow scrapes the [documentation site](https://docs.videodb.io) to generate a doc tree JSON.  

- **Filtering:** The workflow uses the `include` and `exclude` patterns from the configuration to determine which documents should be processed  only the relevant documentation is selected.(it uses doc tree JSON to see hierarchical strucutue)  

- **Crawling:** Each selected document is then crawled using [FireCrawl](https://www.firecrawl.dev/) to retrieve its content. The crawler converts the fetched content into a Markdown format.  

- **LLM Processing:**  The Markdown output of each document is processed through an LLM for summarization and refinement. The prompt used by the LLM is configurable through the prompts settings in the configuration file using `prompts` key, allowing for customized processing of each document. 


- **Consolidation:**  All LLM-processed Markdown outputs are consolidated into a single file and saved as the final documentation context output. 

- **Commit & PR:** Finally, it commits and pushes the changes (or opens a pull request) to update the docs context in the repository.

### 📌 Examples Context Updates
---

[View Github Workflow File »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_examples_context.yml)

This workflow automates the update of the example notebooks Context (IPYNB files) from [VideoDB's Cookbook Repository](https://github.com/video-db/videodb-cookbook)

#### Trigger:

- **Manual Trigger:** : The workflow can be initiated manually via `workflow_dispatch` in the GitHub Actions UI.

- **Event-Based Trigger:** It can also be triggered by a `repository_dispatch` event with the type `examples-context-update`.

#### Workflow:

- **Clone & Setup:** Clones the latest version of the [VideoDB Cookbook repository](https://github.com/video-db/videodb-cookbook)

- **Filtering:** The workflow uses the `include` and `exclude` patterns from the configuration to determine which notebooks should be processed only the relevant documentation is selected.

- **Convert to Markdown**:  Each selected notebook is converted to Markdown using [nbconvert](https://github.com/jupyter/nbconvert)

- **LLM Processing:**  The Markdown output of each notebook is processed through an LLM for summarization and refinement. The prompt used by the LLM is configurable through the prompts settings in the configuration file using `prompts` key, allowing for customized processing of each document.

- **Consolidation:** All LLM-processed Markdown outputs from the notebooks are merged into a single consolidated Markdown file.

- **Commit & PR:** Finally, it commits and pushes the changes (or opens a pull request) to update the examples context in the repository.

### 📌 Update Master Context (llms-full.txt & llms.txt)
---

[View Github Workflow File »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_master_context.yml)

This workflow automates the consolidation of documentation outputs from multiple source contexts (SDK context, Docs context, and Examples context) into two distinct master files. 
- **llms-full.txt** (and its Markdown variant, **llms-full.md**) 
- **llms.txt** (and its Markdown variant, **llms.md**)

Additionally, the workflow updates token statistics and creates a new minor version tag based on the consolidated output.


#### Trigger:

- **Automatic Trigger:** Automatically triggered on push events that affect Markdown files.

- **Manual Trigger:** Manually via `workflow_dispatch` in the GitHub Actions UI.

#### Workflow

- **Merge Full Documentation:** The workflow runs the merge script defined in `llms_full_txt_file.merge_script_path` to combine complete outputs from the Instructions, SDK Context, Docs Context, and Examples Context. The resulting files (**llms-full.txt** and **llms-full.md**) represent the full, consolidated documentation.

- **Token Counting:** Executes the token counting script (using tiktoken) to calculate the number of tokens in the master files and updates the README accordingly.

- **Commit Changes:** The workflow commits the updated master files (both full and fragment-based) and directly pushes changes to `main `branch 

- **Create New Tag:** A new minor version tag is created by incrementing the current tag’s minor version, aiding version tracking and release management.


## ⬆️ Updating LLM Context File

**Step 1: Identify the Subcomponent**

Determine which subcomponent you need to update:

- **SDK Context**
- **Documentation Context**
- **Examples Context**

Each subcomponent has its own GitHub workflow for updates:

| Subcomponent          | Workflow Link                                                                                             | Trigger Method |
|-----------------------|-----------------------------------------------------------------------------------------------------------|----------------|
| **SDK Context**       | [update_sdk_context.yml](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_sdk_context.yml)       | Manual/Event   |
| **Documentation**     | [update_docs_context.yml](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_docs_context.yml)     | Manual         |
| **Examples**          | [update_examples_context.yml](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_examples_context.yml) | Manual/Event   |

**Step 2: Run GitHub Action**

- Navigate to the [GitHub Actions UI](https://github.com/video-db/agent-toolkit/actions).
- Choose the corresponding workflow (SDK, Docs, or Examples).
- Initiate the action:
  - **Manual Trigger**: Click `Run workflow`.
  - **Event-based Trigger**: Trigger via repository dispatch events.


**Step 3: Review & Merge**

The Github Action when finished will raise a Pull Request:
- Verify accuracy
- Merge the PR to officially update context files

> 🪄 Master File(llms-full.txt) will be updated automatically once any sub-component gets updated

## ⚙️ Configuration Options  

To customize or adjust the updating process, modify settings in the central `config.yaml` file located at the repository root.

- Adjust inclusion/exclusion patterns
- Customize LLM processing prompts
- Define source URLs, directories, and output paths



## ⚙️ Configuration Options for Github Actions

All Github Actions takes configuration from `config.yaml` 

You can configure the output of Context using a central config.yaml file available at repository root 

This sections provides details about configuration of each section

`Config key: config.yaml/sdk_context`
  - `clone_url`: The URL of the SDK repository to clone (e.g : https://github.com/video-db/videodb-python).
  - `clone_dir`: The local directory where the SDK repository will be cloned (e.g., `context/sdk/source`).
  - `sphinx_config_dir`: The directory containing the Sphinx configuration (e.g., `context/sdk/sphinx_config`).
  - `output_dir`: The directory where Sphinx generates the documentation output (e.g., `context/sdk/context`).
  - `commit_message`: The commit message used when committing the generated Sphinx Markdown output.
  - `branch_name`:  The branch name to which the changes are pushed.

#### ⚙️ Configuration:    
  
`Config path: config.yaml/docs_context.doc_tree_scrape_config`
  - `script`: The crawler script (e.g., `context/docs/crawl_coda_tree.py`).
  - `output`: The JSON file path where the scraped doc tree is stored (e.g., `context/docs/doc_tree.json`).
  - `url`, `selector`, `selector_value`: Parameters used to scrape the documentation site (e.g., `https://docs.videodb.io` and corresponding HTML attributes).

`Config key: config.yaml/docs_context`
  - `include` & `exclude`: A list of glob-like patterns that determine which  pages from the scraped documentation tree should be included & excluded in the final output.   

    > *Example: This config will include all pages & subpages under [Welcome to Videodb Docs](https://docs.videodb.io/), [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38), [Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80) except [Quickstart Guide/Collections](https://docs.videodb.io/collections-68)*

    ```yaml
    include:
      - "Welcome to Videodb Docs"
      - "Quick Start Guide/*"
      - "Visual Search and Indexing/*"
    exclude:
      - "Quick Start Guide/Collections"

    ```
  - `prompts`: This section has config for how the content should be refined using an LLM during the processing phase.
    - `prompt_folder`: The path to folder which has prompt
    - `default_folder`: The file name of the default prompt should be used in llm processing part for the documents 
    - `custom_prompt`: A list with keys `pattern` and `prompt`, which specifies overriding prompt for a file or pattern  
  
    > *Example: This configuration ensures that, while most of the documentation will be processed using the default prompt, any pages under [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38) will be refined using a specialized prompt that may better suit their content and structure*
  
    ```yaml
    prompts:
      prompt_folder: "context/prompts" 
      default_prompt: "default_docs.txt" 
      custom_prompts:
        - pattern: "Quick Start Guide/*" .
          prompt: "custom_quickstart.txt"
    ```

  -  `base_url`: The base URL for the documentation site. This is used to resolve any relative links that are found during scraping.
  - `tree_file`: Specifies the location of the JSON file that stores the scraped documentation tree. This file is generated by the crawler and later used to filter and process the content.
  - `output_file`: The path where the consolidated Markdown output for the docs context will be written. This file will contain the final, merged documentation content.
  - `script_path`: The path to the processing script that converts the scraped doc tree (and other docs data) into a consolidated Markdown file
  - `branch_name` : The name of the branch that will be used when committing and pushing the updated docs context. This allows the update to be reviewed via a pull request before merging.
  - `commit_message`: The commit message used when updating the docs context. This message describes the changes made by the workflow.



#### ⚙️ Configuration

`Config key: config.yaml/examples_context`

- `include` & `exclude`:
  A list of glob-like patterns that determine which IPYNB notebooks should be included & excluded for processing.  
  *Example: This config will include all notebooks under [quickstart](https://github.com/video-db/videodb-cookbook/tree/main/quickstart) and [guides](https://github.com/video-db/videodb-cookbook/tree/main/guides) except [guides/VideoDB_Search_and_Evaluation](https://github.com/video-db/videodb-cookbook/blob/main/guides/VideoDB_Search_and_Evaluation.ipynb)
  ```yaml
  include:
    - "quickstart/*"
    - "guides/*.ipynb" 
  exclude:
    - "guides/VideoDB_Search_and_Evaluation.ipynb"
  ```

- `prompts`: This section has config for how the content should be refined using an LLM during the processing phase.
  - `prompt_folder`: The path to folder which has prompt
  - `default_folder`: The file name of the default prompt should be used in llm processing part for the documents 
  - `custom_prompt`: A list with keys `pattern` and `prompt`, which specifies overriding prompt for a file or pattern  
  

  > *Example: This configuration ensures that, while most of the ipynbs will be processed using the default prompt, but Multimodal Quickstart will be refined using a specialized prompt that may better suit its content and structure*

  ```yaml
  prompt_folder: "context/prompts"
  default_prompt: "default_ipynb.txt"
  custom_prompts:
    - pattern: "quickstart/Multimodal_Quickstart.ipynb"
      prompt: "custom_2.txt"
  ```

- `clone_url`  
  The URL of the repository containing the example notebooks.  
  > *Example:* https://github.com/video-db/videodb-cookbook

- `clone_dir`  
  The local directory where the repository will be cloned.  
  > *Example: context/examples/source*

- `script_path` 
  The path to the processing script that converts and consolidates the notebooks into Markdown.  
  > *Example: context/examples/process_examples.py*

- `output_file`  
  The file path where the consolidated Markdown output will be written.  
  > *Example: context/examples/examples_context.md*

- `branch_name` 
  The branch name to which the processed output is committed.  

- `commit_message` 
  The commit message used when updating the examples context.  


#### Configuration:

The workflow uses settings from multiple sections in `config.yaml`:

**For the Full Documentation Merge (llms-full.txt / llms-full.md)**
**Config key:** `config.yaml/llms_full_txt_file`

- `merge_script_path`:  
  The path to the script that merges complete documentation outputs.  
  >*Example:* "context/merge_llms_full_txt.py"

- `input_files`:  
  A list of source files with their names and paths:
  - Instructions 
  - SDK Context 
  - Docs Context 
  - Examples Context 

  > Example: it takes all sub components and merge them
  ```yaml
  input_files:
    - name: Instructions
      file_path: "context/instructions/prompt.md"
    - name: SDK Context
      file_path: "context/sdk/context/index.md"
    - name: Docs Context
      file_path: "context/docs/docs_context.md"
    - name: Examples Context
      file_path: "context/examples/examples_context.md"
  ```

- `output_files`:  
  The final output file paths:
  - **llms_full_txt:** e.g., "context/llms-full.txt"
  - **llms_full_md:** e.g., "context/llms-full.md"

- `layout`:  
  A template defining how the input files are merged, using placeholders like `{{FILE1}}`, `{{FILE2}}`, etc.

**Token Count Settings**

`Config path: config.yaml/token_count`

- `script_path`: The path to the token count script (e.g., "context/count_tokens.py")
- `tiktoken_encoding_model`: Specifies the model encoding (e.g., "gpt-4")
- `token_breakdown_file`, `readme_shields_file`: Additional files for reporting (if applicable)



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