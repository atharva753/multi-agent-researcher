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
# 🧠 Multi-Agent Researcher

An intelligent, modular **Multi-Agent AI Assistant** that performs deep research on user queries using large language models (LLMs). It supports custom use cases like academic summarization, code reviews, startup validation, and document summarization — all through a clean Streamlit UI and backend agent orchestration.

---

## 🚀 Features

- 🧩 **Modular Agents** – Agents for search, summarization, and writing  
- 📄 **PDF/TXT Uploader** – Upload your own files for instant summarization  
- 🤖 **Model Selector** – Choose from `deepseek-coder`, `mistral`, or `phi3` via Ollama  
- 🎯 **Use Case Picker** – Academic, Code Review, Startup Validator modes  
- 🧠 **Tone Control** – Objective, critical, optimistic, balanced, skeptical  
- 💬 **Chat History + Export** – Session logs with download as `.md` or `.txt`  
- 🌐 **Streamlit Frontend** – Fast, interactive, and local web-based interface  
- ⚙️ **FastAPI Backend (MCP Server)** – Modular command endpoint system

---

## 📁 Folder Structure

```
multi-agent-researcher/
├── mcp_server.py             # Starts MCP agent backend
├── streamlit_ui.py           # Frontend interface
├── multi_agents/
│   └── main.py               # Agent controller functions
├── server/
│   └── fastmcp.py            # Lightweight FastAPI-based agent orchestration
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/atharva753/multi-agent-researcher.git
cd multi-agent-researcher
```

### 2. Setup virtual environment
```bash
python -m venv .venv
.\.venv\Scripts ctivate      # On Windows
# OR
source .venv/bin/activate     # On macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
```bash
cp .env.example .env
```

### 5. Pull model(s) via Ollama
```bash
ollama pull deepseek-coder
ollama pull mistral
ollama pull phi3
```

---

## 🧪 Running the App

### Start the backend (MCP server)
```bash
python mcp_server.py
```

 MCP Server Running
![MCP Server](screenshots/mcp-server.png)  
FastAPI‑based MCP server registering `deep_research` and `summarize_file` tools and listening on port 8000.

### Start the frontend (Streamlit UI)
```bash
streamlit run streamlit_ui.py
```

Go to: [http://localhost:8501](http://localhost:8501)

Streamlit Home Interface
![UI Home](screenshots/ui-home.png)  
Streamlit UI showing the home screen with model selector, tone picker, and use-case dropdown.
---

## 🧠 Use Cases

| Mode             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Academic**     | Research summaries, paper breakdowns, and fact-based explorations           |
| **Code Review**  | Paste code or upload a `.txt` snippet to get AI insights and improvements   |
| **Startup Validator** | Idea checks, SWOT-style validation, and execution risk summaries       |
| **PDF Summarizer** | Upload a PDF and extract a 1-click agent-generated summary                |

---

## 🌍 Deploy Anywhere

### ✅ Streamlit Cloud
1. Push this repo to your GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Link the repo and point to `streamlit_ui.py`
4. Add environment variables if needed (e.g., `OLLAMA_HOST`)

### ✅ Hugging Face Spaces *(if you remove Ollama dependency)*  
1. Replace local models with hosted LLM APIs (OpenAI, Anthropic, Groq, etc.)
2. Deploy `streamlit_ui.py` as an app

---

## 🙋 Who is This For?

- Students exploring **multi-agent AI workflows**
- Developers building **domain-specific AI assistants**
- Recruiters evaluating **applied AI, LangChain, or Ollama experience**
- Teams experimenting with **RAG pipelines, summarization, or UI agents**

## 🧠 Example Use Cases

- **Academic Paper Summarization** – Upload papers and get fast summaries

![PDF Summary](screenshots/ui-pdf-summary.png)  
*Uploading a PDF and clicking “Summarize File” to get a concise summary of the document content.*


- **Code Review** – Find issues and refactor suggestions in pasted/uploaded code

Code Review Use Case
![Code Review](screenshots/ui-code review.png)  
*Using the Code Review mode with Mistral and Critical tone to analyze and suggest improvements on a snippet of code.*


- **Startup Validator** – Validate your business ideas using agent SWOT analysis
- **Topic Deep-Dives** – Query complex topics (e.g., climate tech) and get multi-agent synthesis

After Running a Research Query
![UI Response](screenshots/ui-response.png)  
*Result of asking “What are the latest trends in green hydrogen tech?” using Mistral with Critical tone, showing chat history and export option.*

- **Policy/Report Summarization** – Drop in PDFs and extract key takeaways instantly


---

## 🧷 Badges

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![Backend](https://img.shields.io/badge/Backend-FastAPI-blue)
![Model](https://img.shields.io/badge/Model-Ollama-cc00ff)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🤝 Contributing

Pull requests welcome! You can:
- Add new agent tools
- Improve the UI
- Add integrations (e.g., real-time web search, vector store, OpenAI tools)

---
### Start Streamlit UI
```bash
streamlit run streamlit_ui.py
```

Open [http://localhost:8501](http://localhost:8501).
