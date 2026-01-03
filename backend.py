#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel, Field
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

ALLOWED_MODELS_NAMES = ["llama3-70b-8192", "llama-3.1-8b-instant", "gpt-4o-mini"]


#Step2: Setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from agents import get_response_from_ai_agent


app = FastAPI(title = "LangGraph AI Agent")

@app.post("/chat") # post request means we are sending data to the server to create/update a resource
async def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODELS_NAMES:
        return {"error": "Model not supported. Please Choose from: " + ", ".join(ALLOWED_MODELS_NAMES)}
    
    #Create AI Agent and get response
    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider
    )
    return response

#Step3: Run app & Explore swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)