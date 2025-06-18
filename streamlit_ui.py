# streamlit_ui.py

import streamlit as st
import os, tempfile
import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = "http://localhost:8000"

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 Multi‑Agent Researcher")

# Sidebar
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Model", ["deepseek-coder","mistral","phi3"])
use_case = st.sidebar.selectbox("Use Case", ["Academic","Code Review","Startup Validator"])
tone = st.sidebar.selectbox("Tone", ["objective","critical","optimistic","balanced","skeptical"])
export_fmt = st.sidebar.selectbox("Download As", ["Markdown","Text"])

if st.sidebar.button("Clear History"):
    st.session_state.history = []

# File uploader + summarization
uploaded = st.sidebar.file_uploader("Upload PDF or TXT", type=["pdf","txt"])
if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded.name)[1]) as tmp:
        tmp.write(uploaded.read())
        filepath = tmp.name
    st.sidebar.success(f"Loaded {uploaded.name}")
    if st.sidebar.button("Summarize File"):
        with st.spinner("Summarizing file..."):
            resp = requests.post(f"{API_URL}/summarize_file", json={"filepath": filepath, "tone": tone})
            data = resp.json()
            summary = data.get("summary", "(no summary)")
            st.session_state.history.append(("📝 File Summary", summary))

# Main query input
query = st.text_input("Enter research query")
if st.button("Run Research"):
    if not query:
        st.error("Please enter a query.")
    else:
        st.session_state.history.append(("You", query))
        with st.spinner("Running agents..."):
            payload = {"query": query, "tone": tone, "model": model, "use_case": use_case}
            resp = requests.post(f"{API_URL}/deep_research", json=payload)
            data = resp.json()
            result = data.get("report", "(no report)")
        st.session_state.history.append(("Bot", result))

# Display history
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {msg}")
    elif speaker == "Bot":
        st.markdown(f"**Bot:** {msg}")
    else:
        st.markdown(f"**{speaker}:** {msg}")

# Export
if st.session_state.history:
    content = "\n\n".join(f"{s}: {m}" for s, m in st.session_state.history)
    filename = "research.md" if export_fmt=="Markdown" else "research.txt"
    st.download_button(f"Download as {export_fmt}", content, file_name=filename)
