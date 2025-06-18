import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from server.fastmcp import FastMCP, Context
import asyncio
from multi_agents.main import run_research_task
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Deep Research")

@mcp.tool()
async def deep_research(query: str, tone: str = "objective", ctx: Context = None):
    result = await run_research_task(query=query, tone=tone, stream_output=None)
    return {"status": "success", "result": result}

if __name__ == "__main__":
    mcp.run()
