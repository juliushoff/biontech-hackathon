from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Clinical Trial Intelligence",
    host="0.0.0.0",
    port=8000,
    streamable_http_path="/mcp",
    stateless_http=True,
    json_response=True,
)
