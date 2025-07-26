# Example MCP Server

An example of how to run a [MPC server in Python](https://github.com/modelcontextprotocol/python-sdk).

## Development Setup

### Prerequisites

- Python 3.12 or higher
- [UV](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone the repository:

```sh
git clone <repository-url>
cd mcp-example
```

2. Install dependencies:

```sh
# Install main dependencies
uv sync

# Install development dependencies (for linting, formatting, etc.)
uv sync --extra dev
```

## Running the MCP Server

To run the MCP server with the testing UI, you can execute the following UV command:

```sh
uv run mcp dev main.py
```

## Development Tools

This project uses several development tools for code quality. All tools are configured in `pyproject.toml` and can be run locally:

### Code Formatting and Linting

**Format code with Black:**

```sh
uv run black .
```

**Sort imports with isort:**

```sh
uv run isort .
```

**Lint code with flake8:**

```sh
uv run flake8 .
```

**Type checking with mypy:**

```sh
uv run mypy .
```

### Run All Checks

You can run all the same checks that the CI pipeline runs:

```sh
# Format and lint
uv run black --check .
uv run isort --check-only .
uv run flake8 .
uv run mypy .
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
