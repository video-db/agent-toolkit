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