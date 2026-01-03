# 🤖 LangGraph AI Agent (LLM + Tools + Web Search)

An **end-to-end agentic AI chatbot system** built using **LangGraph ReAct agents**, **FastAPI**, and **Streamlit**, with dynamic model selection and optional **real-time web search**.  
This project demonstrates how modern AI agents reason, use tools, and respond intelligently in a production-like setup.


---

## 🚀 Key Features

- ✅ **Agentic AI using LangGraph (ReAct pattern)**
- 🔀 **Dynamic LLM selection** (Groq / OpenAI)
- 🌐 **Optional Web Search Tool (Tavily)**
- 🧠 **System Prompt Control**
- 🔁 **Multi-turn message handling**
- ⚡ **FastAPI backend with clean API contract**
- 🎨 **Interactive Streamlit UI**
- 🔐 **Environment-based API key management**

---

## 🛠️ Tech Stack

Python
LangGraph
LangChain
Groq LLMs
OpenAI GPT models
Tavily Search
FastAPI
Streamlit
Pydantic
dotenv

## 🧠 How the Agent Works

1. User enters a query via **Streamlit UI**
2. Request is sent to **FastAPI `/chat` endpoint**
3. Backend:
   - Validates request schema
   - Selects LLM provider (Groq / OpenAI)
   - Creates a **LangGraph ReAct Agent**
   - Optionally enables **Tavily Search Tool**
4. Agent reasons → calls tools (if needed) → responds
5. Final response is streamed back to UI

This simulates **real-world agent reasoning**, not just text generation.

---

## 🏗️ Project Structure

```text
.
├── agents.py        # LangGraph ReAct agent + tool logic
├── backend.py       # FastAPI backend (API + schema validation)
├── frontend.py      # Streamlit UI
├── .env             # API keys (not committed)
├── info.txt         # Environment & dependency setup notes
└── README.md
