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
        "main.py",
        "--api-key=your-videodb-api-key"
      ],
    }
  }
}
```
