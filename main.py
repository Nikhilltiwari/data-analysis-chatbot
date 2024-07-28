import logging

logging.basicConfig(level=logging.INFO)

from fastapi import FastAPI
from api import upload, analyze, visualize
from services.monitoring import setup_monitoring
from dependencies import get_agent_manager, agent_manager

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    pass

# Include routers with the correct prefixes
app.include_router(upload.router, prefix="/api/v1/upload")
app.include_router(analyze.router, prefix="/api/v1/analyze")
app.include_router(visualize.router, prefix="/api/v1/visualize")

# Setup monitoring
setup_monitoring(app)

@app.get("/")
async def root():
    return {"message": "Welcome to the Data Analysis Chatbot"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)










