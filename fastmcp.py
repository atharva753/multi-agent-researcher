class Context:
    async def report_progress(self, msg, progress): pass
    def info(self, msg): print("[INFO]", msg)

class FastMCP:
    def __init__(self, name):
        self.name = name
        self.tools = {}

    def tool(self):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn
        return decorator

    def run(self):
        print(f"[MCP] Server '{self.name}' running with tools: {list(self.tools.keys())}")
