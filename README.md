[![Latest Number][token-length-shield]][token-length-url]
[![GitHub tag (latest SemVer)][tag-shield]][ tag-url]
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

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
    <a href="https://videodb.io/llms.txt"><strong>llms.txt >></strong></a> 
    <a href="https://videodb.io/llms-full.txt"><strong>llms-full.txt</strong></a>  <br />
    <a href="https://videodb.io/mcp"><strong>MCP</strong></a>
    <br />
  </p>
</p>

# VideoDB Agent Toolkit

The VideoDB Agent Toolkit exposes VideoDB context to LLMs and agents. It enables integration to AI-driven IDEs like Cursor, chat agents like Claude Code etc. This toolkit automates context generation, maintenance, and discoverability. It auto-syncs SDK versions, docs, and examples and is distributed through MCP and `llms.txt` 


## 🚀 Quick Overview

The toolkit offers context files designed for use with LLMs, structured around key components:

`llms-full.txt` — Comprehensive context for deep integration.

`llms.txt` — Lightweight metadata for quick discovery.

`MCP (Model Context Protocol)` — A standardized protocol.

These components leverage automated workflows to ensure your AI applications always operate with accurate, up-to-date context.

## 📦 Toolkit Components

### 1. llms-full.txt ([View »](https://videodb.io/llms-full.txt))

---

`llms-full.txt` consolidates everything your LLM agent needs, including:

- Comprehensive VideoDB overview.

- Complete SDK usage instructions and documentation.

- Detailed integration examples and best practices.

**Real-world Examples:**

- [VideoDB's Director](https://chat.videodb.io) `code-assistant` agent ([View Implementation ](https://github.com/video-db/Director/blob/main/backend/director/agents/code_assitant.py))
- [VideoDB's Discord Bot](https://discord.com/invite/py9P639jGz) to power customer support and community help ([View Implementation ]())
- Integrate `llms-full.txt` directly into your LLM-powered workflows, agent systems, or AI coding environments.

### 2. llms.txt ([View »](https://videodb.io/llms.txt))

---

A streamlined file following the [Answer.AI llms.txt proposal](https://github.com/answerdotai/llms-txt). Ideal for quick metadata exposure and LLM discovery.

> **ℹ️ Recommendation**: Use `llms.txt` for lightweight discovery and metadata integration.  Use `llms-full.txt` for complete functionality.

### 3. MCP (Model Context Protocol)

The VideoDB MCP Server connects with the Director backend framework, providing a single tool for many workflows. For development, it can be installed and used via uvx for isolated environments. For more details on MCPs, please visit [here](https://docs.videodb.io/add-videodb-mcp-server-in-clients-108)

## Install `uv`
We need to install uv first.

For macOS/Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
For Windows:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

You can also visit the installation steps of `uv` for more details [here](https://docs.astral.sh/uv/getting-started/installation)

## Run the MCP Server
You can run the MCP server using `uvx` using the following command

```
uvx videodb-director-mcp --api-key=VIDEODB_API_KEY
```

<br/>
       
## 🧠 Anatomy of LLM Context Files

LLM context files in VideoDB are modular, automatically generated, and continuously updated from multiple sources:

### 🧩 Modular Structure:

- **Instructions** — Best practices and prompt guidelines [View »](https://github.com/video-db/agent-toolkit/blob/main/context/instructions/prompt.md)

- **SDK Context** — SDK structure, classes, and interface definitions [View »](https://github.com/video-db/agent-toolkit/blob/main/context/sdk/context/index.md)

- **Docs Context** — Summarized product documentation [View »](https://github.com/video-db/agent-toolkit/blob/main/context/docs/docs_context.md)

- **Examples Context** — Real-world notebook examples [View »](https://github.com/video-db/agent-toolkit/blob/main/context/examples/examples_context.md)
<img src="./token_breakdown.png" alt="Token Breakdown" width="400"/>



### Automated Maintenance:
- Managed through GitHub Actions for automated updates.
- Triggered by changes to SDK repositories, documentation, or examples.
- Maintained centrally via a [`config.yaml`](https://github.com/video-db/agent-toolkit/blob/readme-refactor/config.yaml) file.

---

## 🛠️ Automation with GitHub Actions

Automatic context generation ensures your applications always have the latest information:

### 🔹 SDK Context Workflow ([View](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_sdk_context.yml))
- **Automatically generates documentation** from SDK repo updates.
- Uses [Sphinx](https://www.sphinx-doc.org/en/master/) for Python SDKs.

### 🔹 Docs Context Workflow ([View](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_docs_context.yml))
- **Scrapes and summarizes documentation** using [FireCrawl](https://www.firecrawl.dev/) and LLM-powered summarization.

### 🔹 Examples Context Workflow ([View](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_examples_context.yml))
- Converts and summarizes notebooks into practical context examples.

### 🔹 Master Context Workflow ([View](https://github.com/video-db/agent-toolkit/blob/main/.github/workflows/update_master_context.yml))
- Combines all sub-components into unified `llms-full.txt`.
- Generates standards-compliant `llms.txt`.
- Updates documentation with token statistics for transparency.

---


## 🛠️ Customization via `config.yaml`

The [`config.yaml`](https://github.com/video-db/agent-toolkit/blob/readme-refactor/config.yaml) file centralizes all configurations, allowing easy customization:

- **Inclusion & Exclusion Patterns** for documentation and notebook processing
- **Custom LLM Prompts** for precise summarization tailored to each document type
- **Layout Configuration** for combining context components seamlessly

`config.yaml` > `llms_full_txt_file` defines how `llms-full.txt` is assembled:

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

## 💡 Best Practices for Context-Driven Development

- **Automate Context Updates:** Leverage GitHub Actions to maintain accuracy.
- **Tailored Summaries:** Use custom LLM prompts to ensure context relevance.
- **Seamless Integration:** Continuously integrate with existing LLM agents or IDEs.

By following these practices, you ensure your AI applications have reliable, relevant, and up-to-date context—critical for effective agent performance and developer productivity.

---

## 🚀 Get Started

Clone the toolkit repository and follow the setup instructions in [`config.yaml`](https://github.com/video-db/agent-toolkit/blob/readme-refactor/config.yaml) to start integrating VideoDB contexts into your LLM-powered applications today.

**Explore further:**
- [VideoDB SDK](https://github.com/video-db/videodb-python)
- [Documentation](https://docs.videodb.io)
- [Cookbook Examples](https://github.com/video-db/videodb-cookbook)

---
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[token-length-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/video-db/agent-toolkit/refs/heads/main/readme_shields.json&style=for-the-badge
[token-length-url]: https://github.com/video-db/agent-toolkit/blob/main/token_breakdown.png
[tag-shield]: https://img.shields.io/github/v/tag/video-db/agent-toolkit?style=for-the-badge
[tag-url]: https://github.com/video-db/agent-toolkit/tags
[stars-shield]: https://img.shields.io/github/stars/video-db/agent-toolkit.svg?style=for-the-badge
[stars-url]: https://github.com/video-db/agent-toolkit/stargazers
[issues-shield]: https://img.shields.io/github/issues/video-db/agent-toolkit.svg?style=for-the-badge
[issues-url]: https://github.com/video-db/agent-toolkit/issues
