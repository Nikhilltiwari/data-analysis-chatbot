from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from camel_agent_manager import CamelAgentManager
from prompt import get_llm_prompt
import requests

router = APIRouter()
agent_manager = CamelAgentManager()

@router.post("/")
async def analyze_query(query: str, filename: str):
    df = agent_manager.retrieve_dataframe(filename)
    if df is None:
        raise HTTPException(status_code=404, detail="File not found")
    
    llm_prompt = get_llm_prompt()
    response = requests.post('OLLAMA_API_URL', json={'prompt': llm_prompt, 'query': query, 'columns': df.columns.tolist()})
    answer = response.json().get('answer')
    
    result = agent_manager.get_agent('analyze').process_query(answer, df)
    return JSONResponse(content={"result": result})
