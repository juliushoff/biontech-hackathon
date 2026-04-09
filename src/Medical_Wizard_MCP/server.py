import os

from fastmcp import FastMCP

mcp = FastMCP(
    name="Medical Wizard MCP",
    host=os.getenv("MCP_HOST", "127.0.0.1"),
    port=int(os.getenv("MCP_PORT", "8000")),
    streamable_http_path=os.getenv("MCP_MOUNT_PATH", "/mcp"),
    stateless_http=True,
    json_response=True,
    version=os.getenv("MCP_VERSION", "local"),
)
