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
- VideoDB SDK usage and documentation
- Integration guidance and practical examples

**Example Use Cases of llms-full.txt**:

- `llms-full.txt` is available at https://videodb.io/llms-full.txt which can be downloaded and integrated in LLM-powered Agents and AI Coding IDEs
- [VideoDB's Director](https://chat.videodb.io) uses `llms-full.txt` to power the `code-assistant` agent [See Implementation ](https://github.com/video-db/Director/blob/main/backend/director/agents/code_assitant.py)
- [VideoDB's Helper Discord Bot](https://discord.com/invite/py9P639jGz) uses `llms-full.txt` to power the helper bot [See Implementation ]()

### 2. llms.txt ([View »](https://videodb.io/llms.txt))

---

A streamlined, standards-compliant file following the [Answer.AI llms.txt proposal](https://github.com/answerdotai/llms-txt) for discoverability and metadata exposure to LLMs during inference.

> **ℹ️ Recommendation**: Use llms.txt for basic discovery and llms-full.txt for comprehensive integration.

### 3. 🚧 MCP (Model Context Protocol)

---

👷 Under active development. Documentation coming soon.

## 🧠 LLM Context Files

The following section details on how llm context files are created

### Components of a LLM Context File

VideoDB’s Context files include following Sub-Components Context :

- **Instructions**: Usage instructions and tips ([View](https://github.com/video-db/agent-toolkit/blob/main/context/instructions/prompt.md))
- **SDK Context**: SDK structure and interface definitions. ([View](https://github.com/video-db/agent-toolkit/blob/main/context/sdk/context/index.md))
- **Docs Context** : Compiled documentation and examples ([View](https://github.com/video-db/agent-toolkit/blob/main/context/docs/docs_context.md))
- **Examples Context** : Cookbook patterns for solving common use cases ([View](https://github.com/video-db/agent-toolkit/blob/main/context/examples/examples_context.md))

Here’s how `llms-full.txt` stack up.
![](./token_breakdown.png)

Each Sub-Component is derived from a dedicated underlying source, ensuring accuracy and consistency. To maintain up-to-date context, automated GitHub Actions are triggered whenever changes occur in the source files of these Sub-Components.

When any Sub-Component Context is updated, the Master Context automatically integrates these changes.

All GitHub Actions configurations are centrally managed through a single `config.yaml` file, simplifying updates, configuration, and automation.

The following section provides detailed descriptions of each GitHub Action workflow.

## Workflows that Updates Sub Components Context

### ⚙️ SDK Context

---

[View Github Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_sdk_context.yml)

**🔁 What it does**:

- Grabs latest SDK code
- Builds docs from the code using Sphinx
- Saves the docs and opens a pull request

**▶️ How it runs:**

- Manually or when triggered by an event ( new changes pushed to [videodb-python](https://github.com/video-db/videodb-python) repo)

**️️⚙️ Configuration** 

`config.yaml` > `sdk_context` 

- `clone_url`:  
  The GitHub URL of the SDK repository used as the source for building the SDK context.

- `sphinx_config_dir`:  
  Path to the directory containing the [Sphinx configuration files](https://www.sphinx-doc.org/en/master/usage/configuration.html).  
  This folder defines how the documentation is built from the SDK source code.

### ⚙️ Docs Context

---

[View Github Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_docs_context.yml)

🔁 **What it does:**

- Scrapes [VideoDB Docs](https://docs.videodb.io)'s Documentation Tree
- Filters relevant pages
- Uses FireCrawl to get markdown output of filtered documents
- Uses LLM to summarize content of each page
- Combines all into one file
- Opens a pull request

▶️ **How it runs:**

- Manually from GitHub

**️️⚙️ Configuration**:

`config.yaml` > `docs_context`

- `include`: glob-like patterns that determine which pages should be included in the final output.

- `exclude`: glob-like patterns that determine which pages should be excluded in the final output.

  **Example Config for `include` & `exclude` key :**  

  ```yaml
  include:
    - "Welcome to Videodb Docs"
    - "Quick Start Guide/*"
    - "Visual Search and Indexing/*"
  exclude:
    - "Quick Start Guide/Collections"
  ```

  This config will include all pages & subpages under [Welcome to Videodb Docs](https://docs.videodb.io/), [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38), [Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80) except [Quickstart Guide/Collections](https://docs.videodb.io/collections-68) page

- `prompt` : Config for prompts that is used when summarizing the parsed documents with LLM.

  **Example Config for `prompts` key :**

  ```yaml
  prompts:
    prompt_folder: "context/prompts"
    default_prompt: "default_docs.txt"
    custom_prompts:
      - pattern: "Quick Start Guide/*" .
        prompt: "custom_quickstart.txt"
  ```

  This configuration ensures that, while most of the documentation will be processed using the default prompt( [context/prompts/default_docs.txt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/default_docs.txt) ), any pages under [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38) will be refined using a specialized prompt ( [context/prompts/custom_quickstart.txt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/custom_quickstart.txt) ) that may better suit their content and structure\*

### ⚙️ Examples Context

---

[View Github Workflow »](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_examples_context.yml)

 🔁 **What it does:**

- Clones example notebooks from [Cookbook repo](https://github.com/video-db/videodb-cookbook)
- Filters selected notebooks
- Converts to Markdown
- Uses LLM to summarize them
- Combines into one file
- Opens a pull request

▶️ **How it runs:**

- Triggered by an event (new changes pushed to [videodb-cookbook](https://github.com/video-db/videodb-cookbook) repo)
- Manually

**️️⚙️ Configuration**:

`config.yaml` > `examples_context`

- `include`: glob-like patterns that determine which notebooks should be included in the final output.

- `exclude`: glob-like patterns that determine which notebooks should be excluded in the final output.

  **Example config for `include` & `exclude` key**:

  ```yaml
  include:
    - "quickstart/*"
    - "guides/*.ipynb"
  exclude:
    - "guides/VideoDB_Search_and_Evaluation.ipynb"
  ```

  This config will include all notebooks under [quickstart](https://github.com/video-db/videodb-cookbook/tree/main/quickstart) and [guides](https://github.com/video-db/videodb-cookbook/tree/main/guides) except [guides/VideoDB_Search_and_Evaluation](https://github.com/video-db/videodb-cookbook/blob/main/guides/VideoDB_Search_and_Evaluation.ipynb)

- `prompt` : Config for prompts that is used when summarizing the parsed notebooks with LLM.

  **Example config for `prompt` key**:

  ```yaml
  prompt_folder: "context/prompts"
  default_prompt: "default_ipynb.txt"
  custom_prompts:
    - pattern: "quickstart/Multimodal_Quickstart.ipynb"
      prompt: "custom_2.txt"
  ```

  This configuration ensures that, while most of the ipynbs will be processed using the default ipynb( [context/prompts/default_ipynb.txt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/default_ipynb.txt) ), but Multimodal Quickstart will be refined using a specialized prompt ( [context/prompts/custom_quickstart.txt](https://github.com/video-db/agent-toolkit/blob/main/context/prompts/custom_quickstart.txt) )t that may better suit its content and structure\*


---

### Workflows that Updates Master Context

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
