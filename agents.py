# Step 1 : Setup API Keys for Groq, OpenAI and Tavily  
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


Groq_api_key = os.environ.get("Groq_api_key")
Tavily_api_key = os.environ.get("Tavily_api_key")
Open_api_key = os.environ.get("Open_api_key")


# Step 2 : LLM and Tools setup

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


#openai_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=Open_api_key)
#groq_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, groq_api_key=Groq_api_key)


search_tools = TavilySearch(api_key=Tavily_api_key, num_results=2)


# Step 3: Set up Ai agent with serach tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm = ChatGroq(model=llm_id, groq_api_key=Groq_api_key)
    elif provider=="OpenAI":
        llm = ChatOpenAI(model=llm_id, openai_api_key=Open_api_key)

    tools = [TavilySearch(api_key=Tavily_api_key, num_results=2)] if allow_search else []
    
    agent = create_react_agent(
        model = llm,
        tools = tools
    )
    # ✅ If query is a list of strings, join them into one string
    if isinstance(query, list):
        query_text = "\n".join(query)
    else:
        query_text = str(query)

    # ✅ Proper message structure
    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query_text)
        ]
    }
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1] if ai_messages else "No response generated."
    
# # ✅ Works across versions
# if isinstance(response, AIMessage):
#     print(response.content)
# elif isinstance(response, dict) and "messages" in response:
#     print(response["messages"][-1].content)
# else:
#     print("Unexpected response format:", type(response))
#     print(response)
#-----
