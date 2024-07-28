from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from camel_agent_manager import CamelAgentManager
from dependencies import get_agent_manager

router = APIRouter()

class VisualizeRequest(BaseModel):
    task: str
    query: str
    filename: str

@router.post("")
async def visualize_data(request: VisualizeRequest, agent_manager: CamelAgentManager = Depends(get_agent_manager)):
    try:
        dataframe = agent_manager.retrieve_dataframe(request.filename)
        if dataframe is None:
            raise HTTPException(status_code=404, detail="File not found")
        
        # Process the query using the agent manager
        response = agent_manager.process_query(request.task, request.query, dataframe)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





