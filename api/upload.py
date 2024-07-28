from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import io
from camel_agent_manager import CamelAgentManager

router = APIRouter()
agent_manager = CamelAgentManager()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(await file.read()))
        processed_df = agent_manager.process_query('preprocess', "Preprocess the dataframe", df)
        agent_manager.store_dataframe(file.filename, processed_df)
        return JSONResponse(content={"message": "File uploaded successfully", "columns": processed_df.columns.tolist()})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))





