from fastmcp import FastMCP

mcp = FastMCP("research-assistant")


@mcp.tool()
def search_notes(query: str) -> list[str]:
    """Search the local research notes for a keyword.

    Args:
        query: The keyword or phrase to search for.
    """
    notes = [
        "MCP exposes tools and resources to a model.",
        "A tool performs an action; a resource provides read-only context.",
        "The isError flag signals a tool failure back to the model.",
    ]
    return [n for n in notes if query.lower() in n.lower()]


@mcp.tool()
def word_count(text: str) -> int:
    """Count the number of words in a piece of text.

    Args:
        text: The text to count words in.
    """
    return len(text.split())


@mcp.resource("config://about")
def about() -> str:
    """Static info about this research assistant server."""
    return "Research assistant MCP server — CCA-F practice project."


if __name__ == "__main__":
    mcp.run()
