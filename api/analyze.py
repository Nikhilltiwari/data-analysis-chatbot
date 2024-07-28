from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from camel_agent_manager import CamelAgentManager

router = APIRouter()
agent_manager = CamelAgentManager()

@router.post("/")
async def analyze_query(query: str, filename: str):
    df = agent_manager.retrieve_dataframe(filename)
    if df is None:
        raise HTTPException(status_code=404, detail="File not found")

    result = agent_manager.process_query('analyze', query, df)
    return JSONResponse(content={"result": result})




