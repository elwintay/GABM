from typing import Union
from scripts import gemini
import json
from scripts import agent
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user/prompt/{name}")
def get_user_prompt(name: str):
    try:
        new_agent = agent.Agent(name)
        new_agent.set_agent()
        return {"User Prompt": new_agent.get_user_prompt()}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/user/generate/{name}")
def generate_prompt(name: str):
    try:
        new_agent = agent.Agent(name)
        new_agent.set_agent()
        new_gemini = gemini.Gemini(new_agent)
        response = new_gemini.get_response()
        updated_response = new_agent.set_user_prompt()
        return {"response": updated_response}
    except Exception as e:
        return {"error": str(e)}
