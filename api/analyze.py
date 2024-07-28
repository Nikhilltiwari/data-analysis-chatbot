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
        logging.info(f"Received analyze request: {request}")

        dataframe = agent_manager.retrieve_dataframe(request.filename)
        if dataframe is None:
            logging.error("File not found")
            raise HTTPException(status_code=404, detail="File not found")

        logging.info(f"Dataframe shape for analysis: {dataframe.shape}")

        # Process the query using the agent manager
        response = agent_manager.process_query(request.task, request.query, dataframe)
        logging.info(f"Analysis response: {response}")

        return {"response": response}
    except Exception as e:
        logging.error(f"Error analyzing data: {e}")
        raise HTTPException(status_code=500, detail=str(e))







