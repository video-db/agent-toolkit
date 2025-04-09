To add the MCP server in any config driven MCP Client, following is how the commands and arguments will look like

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

```uvx videodb-director-mcp --install=all```
