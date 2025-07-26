from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Example MCP Server")


@mcp.prompt("say_hello")
def hello(name: str) -> str:
    """
    Say hello to a person.
    """
    return f"Say hello to {name} in a friendly way!"


@mcp.resource("file://introduction")
def introduce() -> str:
    """
    Introduce yourself to a person.
    """
    with open("resources/introduction.md", "r") as file:
        return file.read()


@mcp.tool("write_reply")
def reply(message: str) -> str:
    """
    Reply to a message.
    """
    return f"You said: {message}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
