from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from pandas import read_csv, read_excel
from io import BytesIO
from camel_agent_manager import CamelAgentManager
from dependencies import get_agent_manager
import logging
import mimetypes

router = APIRouter()

@router.post("")
async def upload_file(file: UploadFile = File(...), agent_manager: CamelAgentManager = Depends(get_agent_manager)):
    try:
        logging.info(f"Received file: {file.filename}")
        contents = await file.read()
        file_extension = file.filename.split('.')[-1].lower()
        mime_type, _ = mimetypes.guess_type(file.filename)

        logging.info(f"File extension: {file_extension}")
        logging.info(f"MIME type: {mime_type}")
        logging.info(f"First 100 bytes of file content: {contents[:100]}")

        if file_extension == 'csv' or 'csv' in mime_type:
            dataframe = read_csv(BytesIO(contents))
        elif file_extension in ['xls', 'xlsx'] or mime_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            dataframe = read_excel(BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        logging.info(f"Dataframe shape: {dataframe.shape}")

        filename = file.filename
        agent_manager.store_dataframe(filename, dataframe)
        logging.info(f"Stored dataframe with filename: {filename}")

        return {"filename": filename, "message": "File uploaded successfully"}
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))











