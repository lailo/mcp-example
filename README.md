# Example MCP Server

An example of how to run a [MPC server in Python](https://github.com/modelcontextprotocol/python-sdk).

## Development

To run the MCP server with the testing UI, you can execute the following UV command:

```sh
uv run mcp dev main.py
```

## Configuration

The following configuration is for the Claude desktop client.

```JSON
{
  "mcpServers": {
    "mcp-example": {
      "command": "uv",
      "args": [
        "--directory",
        "___PATH_TO_THIS_REPOSITORY___",
        "run",
        "main.py"
      ]
    }
  }
}
```
