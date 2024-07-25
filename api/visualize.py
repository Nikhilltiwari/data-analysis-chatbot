from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from camel_agent_manager import CamelAgentManager

router = APIRouter()
agent_manager = CamelAgentManager()

@router.post("/")
async def visualize(query: str, filename: str):
    df = agent_manager.retrieve_dataframe(filename)
    if df is None:
        raise HTTPException(status_code=404, detail="File not found")
    plot_url = agent_manager.get_agent('visualize').create_plot(query, df)
    return JSONResponse(content={"plot_url": plot_url})


