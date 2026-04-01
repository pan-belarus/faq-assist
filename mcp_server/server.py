from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Text Analysis Server")


@mcp.tool()
def count_letters(text: str, search: str) -> int:
    return text.lower().count(search.lower())


@mcp.resource("greeting://{who}")
def get_greeting(who: str) -> str:
    return f"Hello, {who}!"


@mcp.prompt(title="Count Letters")
def count_letters_prompt(text: str, search: str) -> str:
    return f"Count the occurrences of the letter '{search}' in the text:\n\n{text}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")