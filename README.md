# Multi-Agent Researcher

## Setup

1. Clone this repo
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and adjust.

## Running

### Start MCP Server
```bash
python mcp_server.py
```

### Start Streamlit UI
```bash
streamlit run streamlit_ui.py
```

Open [http://localhost:8501](http://localhost:8501).
