from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from camel_agent_manager import CamelAgentManager
from services.nlp import analyze_query_with_llm

router = APIRouter()
agent_manager = CamelAgentManager()

@router.post("/")
async def analyze_query(query: str, filename: str):
    df = agent_manager.retrieve_dataframe(filename)
    if df is None:
        raise HTTPException(status_code=404, detail="File not found")

    llm_response = analyze_query_with_llm(query, df.columns.tolist())
    result = agent_manager.get_agent('analyze').process_query(llm_response, df)
    return JSONResponse(content={"result": result})

