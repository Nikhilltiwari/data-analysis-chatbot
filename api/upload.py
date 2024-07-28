from fastapi import APIRouter, UploadFile, File, HTTPException
from pandas import read_csv, read_excel
from io import BytesIO
from camel_agent_manager import CamelAgentManager

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_extension = file.filename.split('.')[-1].lower()
        
        if file_extension == 'csv':
            dataframe = read_csv(BytesIO(contents))
        elif file_extension in ['xls', 'xlsx']:
            dataframe = read_excel(BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        filename = file.filename
        agent_manager.store_dataframe(filename, dataframe)
        return {"filename": filename, "message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




