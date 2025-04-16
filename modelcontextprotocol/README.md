[![smithery badge](https://smithery.ai/badge/@video-db/agent-toolkit)](https://smithery.ai/server/@video-db/agent-toolkit)

To add the MCP server in any config driven MCP Client, following is how the commands and arguments will look like

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

## Add the VideoDB Director MCP Server in your favorite Client

### Claude Desktop

To configure VideoDB Director MCP server in Claude, you can run the following command

```uvx videodb-director-mcp --install=claude```

You can manually configure the MCP Server by following these steps:

1. Open the `claude_desktop_config.json` file

   In MacOS/Linux:

   ```
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

   In Windows:

   ```
   code $env:AppData\Claude\claude_desktop_config.json
   ```

2. Add the VideoDB Director MCP Server inside the `mcpServers` key:

   ```json
   {
     "mcpServers": {
       "videodb-director": {
         "command": "uvx",
         "args": ["videodb-director-mcp", "--api-key=<VIDEODB-API-KEY>"]
       }
     }
   }
   ```

### Cursor

To configure VideoDB Director MCP server in Cursor, you can run the following command

```uvx videodb-director-mcp --install=cursor```

You can manually configure the MCP Server by following these steps:

1. Inside Cursor, go to **Settings > Cursor Settings**
2. Click on **MCP**
3. Click on **Add new Global MCP Server**
4. Add the VideoDB Director MCP Server under the `mcpServers` key

   ```json
   {
     "mcpServers": {
       "videodb-director": {
         "command": "uvx",
         "args": ["videodb-director-mcp", "--api-key=<VIDEODB-API-KEY>"]
       }
     }
   }
   ```

### Install in Claude and Cursor at the same time.
You can configure VideoDB Director MCP server in Claude and Cursor together, by running the following command

```
uvx videodb-director-mcp --install=all
```


### Install for Claude Code

```
claude mcp add videodb-director uvx -- videodb-director-mcp --api-key=<VIDEODB_API_KEY>
```

## Update VideoDB Director MCP package

To ensure you're using the latest version of the MCP server with `uvx`, start by clearing the cache:

```
uv cache clean
```

This command removes any outdated cached packages of `videodb-director-mcp`, allowing `uvx` to fetch the most recent version.

If you always want to use the latest version of the MCP server, update your command as follows:
```
uvx videodb-director-mcp@latest --api-key=<VIDEODB_API_KEY>
```
