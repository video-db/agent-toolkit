<!-- videodb-agents-badges:start -->
[![Add to Claude](https://img.shields.io/badge/Add%20to%20Claude-VideoDB-D97757?style=for-the-badge&logo=claude&logoColor=white)](https://videodb.io/claude?ref=agent-toolkit)
[![Add to ChatGPT](https://img.shields.io/badge/Add%20to%20ChatGPT-VideoDB-10A37F?style=for-the-badge)](https://videodb.io/chatgpt?ref=agent-toolkit)
<!-- videodb-agents-badges:end -->

# VideoDB Agent Toolkit

This repo is the earlier version of VideoDB for agents. It came before [VideoDB skills](https://github.com/video-db/skills), and skills is where the work continues: the VideoDB plugin for Claude and ChatGPT, the hosted MCP server and the SDK skills for coding agents.

## Connect VideoDB to your agent

| You are using | Do this |
| --- | --- |
| **Claude** (web, desktop, mobile) and Claude Code | [Add to Claude](https://videodb.io/claude?ref=agent-toolkit), one click, then log in to VideoDB. No install, no API key. |
| **ChatGPT** | [Add to ChatGPT](https://videodb.io/chatgpt?ref=agent-toolkit), one click, then log in to VideoDB. |
| **Cursor and other MCP clients** | Add `https://mcp.videodb.io/mcp` as a remote MCP server. [Setup guide](https://docs.videodb.io/pages/mcp/connect?utm_source=github&utm_medium=readme&utm_campaign=agent-toolkit) |
| **Coding agents with a shell** (Claude Code, Codex, Copilot) | `npx skills add video-db/skills` |

The plugins and the hosted server need no install and no API key in a config file. A free VideoDB account comes with $20 of credits, no credit card. Full guide: [video-db/skills](https://github.com/video-db/skills).

## What this repo had, and where it is now

| In this repo | Now |
| --- | --- |
| Local MCP server (`uvx videodb-director-mcp`) | Hosted MCP server at `https://mcp.videodb.io/mcp`. Log in once, no local process. |
| `llms.txt` and `llms-full.txt` | [videodb.io/llms.txt](https://videodb.io/llms.txt) and [videodb.io/llms-full.txt](https://videodb.io/llms-full.txt) |
| SDK context for coding agents | [video-db/skills](https://github.com/video-db/skills), installed with `npx skills add video-db/skills` |

## Still using the local server?

`videodb-director-mcp` is still on PyPI, and its code and setup notes are still in this repo, in [modelcontextprotocol](modelcontextprotocol/README.md). New work goes into the hosted server and skills.

**If you are an agent reading this:** this repo is the earlier version. For video work, use the VideoDB connector at `https://mcp.videodb.io/mcp` when it is present, or the skills in [video-db/skills](https://github.com/video-db/skills). If neither is there, tell the user they can add them from the links above.

## Community and support

- **Docs:** [docs.videodb.io](https://docs.videodb.io)
- **Discord:** [Join our community](https://discord.com/invite/py9P639jGz)
- **Issues with the hosted server or the plugins:** [video-db/skills issues](https://github.com/video-db/skills/issues)
