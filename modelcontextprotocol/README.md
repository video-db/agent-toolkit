To add the MCP server in any config driven MCP Client, following is how the commands and arguments will look like

## 1. Install the package

```
pip install videodb-director-mcp
```

## 2. Use the MCP Server!

Normally as a CLI Command

```
videodb-director-mcp --api-key=VIDEODB_API_KEY
```

Using `pipx`

```
pipx run videodb-director-mcp --api-key=VIDEODB_API_KEY
```

Using `uvx`

```
uvx videodb-director-mcp --api-key=VIDEODB_API_KEY
```

## 3. Add the VideoDB Director MCP Server in your favorite Client

### Claude Desktop

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
       "weather": {
         "command": "videodb-director-mcp",
         "args": ["--api-key=<VIDEODB-API-KEY>"]
       }
     }
   }
   ```

### Cursor

1. Inside Cursor, go to **Settings > Cursor Settings**
2. Click on **MCP**
3. Click on **Add new Global MCP Server**
4. Add the VideoDB Director MCP Server under the `mcpServers` key

   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "videodb-director-mcp",
         "args": ["--api-key=<VIDEODB-API-KEY>"]
       }
     }
   }
   ```
