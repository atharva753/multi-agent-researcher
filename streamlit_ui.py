import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

st.title("Multi-Agent Researcher")
model = st.sidebar.selectbox("Choose Model", ["deepseek-coder", "mistral", "phi3"])
query = st.text_input("Research Query")
tone = st.sidebar.selectbox("Tone", ["objective", "critical", "optimistic"])
if st.button("Run Research"):
    st.write(f"Running with model: {model}")
    # Placeholder - integrate with real MCP server
    st.write(f"Result: Research on '{query}' with tone '{tone}' completed.")
