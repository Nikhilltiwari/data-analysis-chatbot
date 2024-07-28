from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from camel_agent_manager import CamelAgentManager
from dependencies import get_agent_manager
import logging

router = APIRouter()

class AnalyzeRequest(BaseModel):
    task: str
    query: str
    filename: str

@router.post("")
async def analyze_data(request: AnalyzeRequest, agent_manager: CamelAgentManager = Depends(get_agent_manager)):
    try:
        logging.info(f"Received analyze request: task='{request.task}' query='{request.query}' filename='{request.filename}'")

        dataframe = agent_manager.get_dataframe(request.filename)
        if dataframe is None:
            raise HTTPException(status_code=404, detail="Dataframe not found")

        logging.info(f"Dataframe shape for analysis: {dataframe.shape}")

        context = {
            'dataframe': dataframe,
            'query': request.query
        }

        # Assuming call_openai_model is a method of CamelAgentManager that needs context
        result = agent_manager.call_openai_model(context)

        return {"result": result}
    except Exception as e:
        logging.error(f"Error analyzing data: {e}")
        raise HTTPException(status_code=500, detail=str(e))







