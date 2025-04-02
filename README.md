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

This repository provides tools and context files for integrating VideoDB into AI applications, LLM-powered agents, and AI coding IDEs.

<br/>

## 📦 Toolkit Components

### 1. llms-full.txt ([View »](https://videodb.io/llms-full.txt))

---

`llms-full.txt` is a complete reference providing:

- Detailed VideoDB background
- VideoDB SDK usage and documentation
- Integration guidance and practical examples realted to VideoDB

**Example Use Cases of llms-full.txt**:

- [VideoDB's Director](https://chat.videodb.io) uses llms-full.txt to power the `code-assistant` agent ([View Implementation ](https://github.com/video-db/Director/blob/main/backend/director/agents/code_assitant.py))
- [VideoDB's Helper Discord Bot](https://discord.com/invite/py9P639jGz) uses llms-full.txt to power the helper bot ([View Implementation ]())
- llms-full.txt can be downloaded and integrated in LLM-powered Agents and AI Coding IDEs

### 2. llms.txt ([View »](https://videodb.io/llms.txt))

---

A streamlined, standards-compliant file following the [Answer.AI llms.txt proposal](https://github.com/answerdotai/llms-txt) for discoverability and metadata exposure to LLMs during inference.

> **ℹ️ Recommendation**: Use llms.txt for basic discovery and llms-full.txt for comprehensive integration.

### 3. MCP (Model Context Protocol)

---

👷 Under active development. Documentation coming soon.

   
<br/>
       
## 🧠 LLM Context Files

This section provides a detailed overview of how LLM context files are structured and maintained within the toolkit.

### 🧩 Components of an LLM Context File

Each LLM context file in VideoDB is composed of multiple sub-components, each sourced and maintained independently. These sub-components come together to form the complete `llms-full.txt` file:

- **Instructions** — Usage guidelines and prompt tips  
  [View »](https://github.com/video-db/agent-toolkit/blob/main/context/instructions/prompt.md)

- **SDK Context** — SDK structure, classes, and interface definitions  
  [View »](https://github.com/video-db/agent-toolkit/blob/main/context/sdk/context/index.md)

- **Docs Context** — Compiled product documentation and usage examples  
  [View »](https://github.com/video-db/agent-toolkit/blob/main/context/docs/docs_context.md)

- **Examples Context** — Practical notebook-based recipes and patterns  
  [View »](https://github.com/video-db/agent-toolkit/blob/main/context/examples/examples_context.md)

---

Here’s how these components stack up within `llms-full.txt`:

![Token Breakdown](./token_breakdown.png)

Each sub-component is automatically generated from its respective source (e.g., SDK repo, documentation site, example notebooks).

To keep everything up-to-date:

- **GitHub Actions** are triggered whenever source content changes
- These workflows regenerate the relevant sub-component context
- A final workflow updates the **Master Context** (i.e., `llms-full.txt` and `llms.txt`)

All configuration is centrally managed via a single  
[`config.yaml`](https://github.com/video-db/agent-toolkit/blob/readme-refactor/config.yaml) file.


<br/>

## 🔧 GitHub Actions for Sub-Component Context Updates

This section describes each GitHub Action workflow responsible for generating and updating **Sub-Component Contexts** from their respective sources.

> **Note**: This guide highlights the **most commonly used configuration options**.  
> To keep things concise, it omits explanations for obvious settings—these can be found in the [`config.yaml`](https://github.com/video-db/agent-toolkit/blob/readme-refactor/config.yaml) file.

<br> 

### ⚙️ SDK Context

---

[View GitHub Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_sdk_context.yml)

**🔁 What it does:**

- Clones the latest version of the [VideoDB SDK](https://github.com/video-db/videodb-python)
- Generates documentation from docstrings using [Sphinx](https://www.sphinx-doc.org/en/master/)
- Saves the generated docs and opens a pull request with the updates

**▶️ How it runs:**

- Automatically triggered when changes are pushed to the `videodb-python` repository

> ℹ️ This is done using [`workflow_dispatch`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch), which allows external repositories to trigger workflows.  
> See how [`videodb-python` triggers this action](https://github.com/video-db/videodb-python/blob/main/.github/workflows/trigger-agent-toolkit-update.yaml)

**️️⚙️ Configuration** 

`config.yaml` > `sdk_context` 

- `clone_url`:  
  GitHub URL of the SDK repository used as the source

- `sphinx_config_dir`:  
  Path to the directory containing the [Sphinx configuration files](https://www.sphinx-doc.org/en/master/usage/configuration.html).  


> 💡 **Note**: This workflow is currently designed for Python SDKs only. 

<br> 

### ⚙️ Docs Context

---

[View Github Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_docs_context.yml)

🔁 **What it does:**

- Scrapes [VideoDB Docs](https://docs.videodb.io)'s [Documentation Tree](https://github.com/video-db/agent-toolkit/blob/readme-refactor/context/docs/doc_tree.json)
- Filters relevant pages
- Uses [FireCrawl](https://www.firecrawl.dev/) to get markdown output of filtered documents
- Uses LLM to summarize content of each page
- Combines all into one file
- Commits the generated files to a seperate branch and Opens a pull request

▶️ **How it runs:**

- Manually from GitHub

**️️⚙️ Configuration**:

`config.yaml` > `docs_context`

- `include` & `exclude` : Specify which documentation pages to process using glob-style patterns:

  **Example Config for `include` & `exclude` key :**  

  ```yaml
  include:
    - "Welcome to Videodb Docs"
    - "Quick Start Guide/*"
    - "Visual Search and Indexing/*"
  exclude:
    - "Quick Start Guide/Collections"
  ```

  > 💡 _This setup will include all pages & subpages under [Welcome to Videodb Docs](https://docs.videodb.io/), [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38), [Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80) except [Quickstart Guide/Collections](https://docs.videodb.io/collections-68) page_
  

- `prompt` : Customize how the LLM summarizes each document:.

  **Example Config for `prompts` key :**

  ```yaml
  prompts:
    prompt_folder: "context/prompts"
    default_prompt: "default_docs.txt"
    custom_prompts:
      - pattern: "Quick Start Guide/*" .
        prompt: "custom_quickstart.txt"
  ```

  > _🧠 Pages under “Quick Start Guide” use a [custom summarization prompt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/custom_quickstart.txt ), while the rest default to [default_docs.txt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/default_docs.txt)._

<br>

### ⚙️ Examples Context

---

[View Github Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_examples_context.yml)

 🔁 **What it does:**

- Clones notebooks from [Cookbook repo](https://github.com/video-db/videodb-cookbook)
- Filters selected notebooks
- Converts selected notebooks to Markdown
- Summarizes each notebook using LLM prompts
- Merges all summaries into a single context file
- Commits the generated files to a seperate branch and Opens a pull request

▶️ **How it runs:**

- Triggered when updates are pushed to the [videodb-cookbook](https://github.com/video-db/videodb-cookbook) repository
- Can also be run manually from GitHub

**️️⚙️ Configuration**:

`config.yaml` > `examples_context`

- `include` & `exclude` : Specify which notebooks to process using glob-style patterns:

  **Example config for `include` & `exclude` key**:

  ```yaml
  include:
    - "quickstart/*"
    - "guides/*.ipynb"
  exclude:
    - "guides/VideoDB_Search_and_Evaluation.ipynb"
  ```

  > _📌 This example includes all notebooks in [quickstart](https://github.com/video-db/videodb-cookbook/tree/main/quickstart) and [guides](https://github.com/video-db/videodb-cookbook/tree/main/guides), but excludes one specific [evaluation notebook](https://github.com/video-db/videodb-cookbook/blob/main/guides/VideoDB_Search_and_Evaluation.ipynb)_

- `prompt` : Customize how the LLM summarizes each document:.

  **Example config for `prompt` key**:

  ```yaml
  prompt_folder: "context/prompts"
  default_prompt: "default_ipynb.txt"
  custom_prompts:
    - pattern: "quickstart/Multimodal_Quickstart.ipynb"
      prompt: "custom_2.txt"
  ```
  > _🧠 Most notebooks are summarized with the [default prompt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/default_ipynb.txt), but key ones like [Multimodal_Quickstart.ipynb](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/custom_quickstart.txt ) use tailored prompt instructions._



<br> <br/>

### Workflows that Updates Master Context
---

The following section provides detailed description, configuration options of GitHub Action workflow that updates master files like `llms-full.txt` & `llms.txt` whenever any sub-component context is updated  

[View GitHub Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_master_context.yml)

**🔁 What it does:**

- Combines all Sub-Component Contexts into a single unified file: `llms-full.txt`
- Generates a standards-compliant `llms.txt` for LLM discoverability
- Updates related token statistics in `README.md`

**▶️ How it runs:**

- Automatically triggered whenever any Sub-Component Context (Instructions, SDK, Docs, Examples) is updated

---

**⚙️ Configuration:**

Defined under multiple keys in [`config.yaml`](https://github.com/video-db/agent-toolkit/blob/readme-refactor/config.yaml):

#### 🔹 llms_full_txt_file

`config.yaml` > `llms_full_txt_file`

Defines how `llms-full.txt` is assembled:

```yaml
llms_full_txt_file:
  input_files:
    - name: Instructions
      file_path: "context/instructions/prompt.md"
    - name: SDK Context
      file_path: "context/sdk/context/index.md"
    - name: Docs Context
      file_path: "context/docs/docs_context.md"
    - name: Examples Context
      file_path: "context/examples/examples_context.md"
  output_files:
    - name: llms_full_txt
      file_path: "context/llms-full.txt"
    - name: llms_full_md
      file_path: "context/llms-full.md"
  layout: |
    {{FILE1}}

    {{FILE2}}

    {{FILE3}}

    {{FILE4}}

  ```
  
  > 🧩 The layout field defines the merge strategy—here, a simple concatenation of all sub-components



#### 🔹 llms_txt_file

Defines how the lightweight llms.txt file is structured.
(See config.yaml for current format and layout.)
`config.yaml` > `llms_txt_file`

**️️⚙️ Configuration for Readme Stastics**:

`config.yaml` > `token_count`
- `tiktoken_encoding_model` : The tiktoken encoding model to use to count LLM Context file tokens


