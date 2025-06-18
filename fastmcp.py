# server/fastmcp.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import inspect
import asyncio

class Context:
    async def report_progress(self, msg, progress): pass
    def info(self, msg): print("[INFO]", msg)

class FastMCP:
    def __init__(self, name: str):
        self.name = name
        self.app = FastAPI(title=name)
        self.tools = {}

        # Allow CORS for frontend access
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def tool(self):
        """
        Decorator to register a function as a tool endpoint.
        """
        def wrapper(fn):
            route = f"/{fn.__name__}"
            self.tools[fn.__name__] = fn

            async def endpoint(req: Request):
                try:
                    data = await req.json()
                    sig = inspect.signature(fn)
                    params = {k: data.get(k) for k in sig.parameters if k != "ctx"}

                    # Inject context if accepted
                    if "ctx" in sig.parameters:
                        result = await fn(**params, ctx=Context())
                    else:
                        result = await fn(**params)
                    return result
                except Exception as e:
                    return {"status": "error", "error": str(e)}

            self.app.post(route)(endpoint)
            print(f"[MCP] Registered tool → POST {route}")
            return fn
        return wrapper

    def run(self, host="0.0.0.0", port=8000):
        """
        Start the FastAPI server with registered tools.
        """
        import uvicorn
        print(f"[MCP] Server '{self.name}' starting on http://{host}:{port}")
        asyncio.run(self._launch_uvicorn(host, port))

    async def _launch_uvicorn(self, host, port):
        config = {"app": self.app, "host": host, "port": port, "reload": False}
        import uvicorn
        uvicorn.run(**config)
