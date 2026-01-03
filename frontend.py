#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

st.title("Your AI CHATBOT ")  
st.set_page_config(page_title="LangGraph AI Agent", page_icon="🤖", layout="centered")
st.write("Interact with your customised AI Agent!")

system_prompt = st.text_area("", placeholder="Type your system prompt here...", height=70)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider:", ("Groq", "OpenAI"))
if provider=="Groq":
    model_name = st.selectbox("Select LLM Model:", MODEL_NAMES_GROQ)
elif provider=="OpenAI":
    model_name = st.selectbox("Select LLM Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Enable Web Search", value=True)

user_query = st.text_area("Enter your query:", placeholder="Ask anything...", height=150)  

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent!"):
    if user_query.strip():          #strip is used to remove any leading/trailing or starting/ending blankspace/ whitespace
    #step2: Connect with backend
        import requests
        payload = {
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(f"Error: {response_data['error']}")
            else:
               st.subheader("Agent's Response:")
               st.markdown(response_data)
