from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

class QueryRequest(BaseModel):
    prompt: str
    context: dict

class QueryResponse(BaseModel):
    response: dict

@app.post("/llama", response_model=QueryResponse)
async def llama(query: QueryRequest):
    if not query.prompt or not query.context:
        raise HTTPException(status_code=400, detail="Invalid request")
    
    # Mock response for demonstration
    response = {
        "response": {key: random.randint(1, 100) for key in query.context['dataframe']}
    }
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
