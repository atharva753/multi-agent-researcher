# multi_agents/main.py

import asyncio
import os
import pdfplumber
from typing import Optional
from dotenv import load_dotenv
from mcp.client import MCPClient   # hypothetical MCP HTTP client wrapper

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

async def run_research_task(query: str, tone: str, model: str, use_case: str, stream_output=None) -> str:
    """
    Sends a request to the MCP server's deep_research tool.
    """
    payload = {
        "query": query,
        "tone": tone,
        "model": model,
        "use_case": use_case
    }
    client = MCPClient("http://localhost:8000")
    result = await client.call_tool("deep_research", payload, stream_output=stream_output)
    return result.get("report", "")

async def summarize_text(filepath: str, tone: str) -> str:
    """
    Extracts text from PDF/TXT and sends it to the summarize_file tool.
    """
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        text = ""
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

    client = MCPClient("http://localhost:8000")
    result = await client.call_tool("summarize_file", {"filepath": filepath, "tone": tone})
    return result.get("summary", "")
