import os
import asyncio
from fastmcp import FastMCP

mcp = FastMCP(
    name="Medical Wizard MCP",
    version=os.getenv("MCP_VERSION", "local"),
)

if __name__ == "__main__":
    asyncio.run(mcp.run_http_async(
        host=os.getenv("FASTMCP_HOST", "0.0.0.0"),
        port=int(os.getenv("FASTMCP_PORT", "8000")),
        stateless_http=True,
        json_response=True,
    ))