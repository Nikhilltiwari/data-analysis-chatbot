from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dependencies import get_agent_manager
import logging

router = APIRouter()
agent_manager = get_agent_manager()

class AnalyzeRequest(BaseModel):
    task: str
    query: str
    filename: str

@router.post("/")
async def analyze_data(request: AnalyzeRequest):
    try:
        df = agent_manager.retrieve_dataframe(request.filename)
        if df is None:
            logging.error(f"Dataframe with filename {request.filename} not found")
            raise HTTPException(status_code=404, detail="File not found")

        response = agent_manager.process_query(request.task, request.query, df)
        return {"response": response}
    except Exception as e:
        logging.error(f"Error analyzing data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error analyzing data: {str(e)}")










