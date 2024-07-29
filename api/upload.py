from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io
from dependencies import get_agent_manager
import logging

router = APIRouter()
agent_manager = get_agent_manager()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        if file.content_type == 'text/csv':
            df = pd.read_csv(io.BytesIO(contents))
        elif file.content_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            df = pd.read_excel(io.BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        agent_manager.store_dataframe(file.filename, df)
        return {"filename": file.filename, "message": "File uploaded successfully"}
    except Exception as e:
        logging.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing file")

















