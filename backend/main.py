from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent
import traceback
import json
import re

app = FastAPI()

class UserInput(BaseModel):
    message: str

def extract_json(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in model output")
    return json.loads(match.group())

@app.post("/agent")
async def run_agent(input: UserInput):
    try:
        result = await agent.run(input.message)
        return extract_json(result.output)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
