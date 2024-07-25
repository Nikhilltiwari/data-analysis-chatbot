from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import io
from services.data_processing import process_data

router = APIRouter()

@router.post('/')
async def upload_file(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(await file.read()))
        processed_df = process_data(df)
        return JSONResponse(content={'message': 'File uploaded successfully', 'columns': processed_df.columns.tolist()})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
