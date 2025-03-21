To add the MCP server in any config driven MCP Client, following is how the commands and arguments will look like

```
{
  "mcpServers": {
    "videodb": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/directory/mcp-server-videodb",
        "run",
        "main.py"
      ],
      "env": {
        "VIDEODB_API_KEY": "your-videodb-api-key"
      }
    }
  }
}
```
