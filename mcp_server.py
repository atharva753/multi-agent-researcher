import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from server.fastmcp import FastMCP, Context
from typing import Dict, Any, Optional
from gpt_researcher.utils.enum import Tone   # or your equivalent enum
import asyncio
from dotenv import load_dotenv
from multi_agents.main import run_research_task, summarize_text

# Load environment variables from .env
load_dotenv()

# Create an MCP server named "Deep Research"
mcp = FastMCP("Deep Research")

# Main research tool
@mcp.tool()
async def deep_research(
    query: str,
    tone: str = "objective",
    model: str = "deepseek-coder",
    use_case: str = "Academic",
    ctx: Context = None
) -> Dict[str, Any]:
    """
    Perform deep research on a given query using multiple AI agents.
    Accepts extra params:
      - model: which Ollama model to use
      - use_case: which template or flow to apply
    
    Returns:
      { status, query, tone, model, use_case, report }
    """
    # Convert tone string to enum
    tone_enum = getattr(Tone, tone.capitalize(), Tone.Objective)

    # (Optionally) you could route to different pipelines based on use_case
    report = await run_research_task(
        query=query,
        tone=tone_enum,
        stream_output=lambda t,k,v,_: None  # no progress reporting here
    )

    return {
        "status": "success",
        "query": query,
        "tone": tone,
        "model": model,
        "use_case": use_case,
        "report": report
    }

# File summarizer tool
@mcp.tool()
async def summarize_file(
    filepath: str,
    tone: str = "objective",
    ctx: Context = None
) -> Dict[str, Any]:
    """
    Summarize text from a local file (PDF or TXT).
    The UI will upload and pass the temp file path here.
    """
    try:
        summary = await summarize_text(filepath, tone)
        return {"status": "success", "summary": summary}
    except Exception as e:
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    # This will register both tools and start listening
    mcp.run()
