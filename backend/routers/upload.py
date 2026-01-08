from fastapi import APIRouter, File, UploadFile, HTTPException, Query
from datetime import datetime
import uuid
from typing import Dict, Any

router = APIRouter(prefix="/api", tags=["upload"])

# This will be injected from main.py
file_service = None
session_data = None

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)) -> Dict[str, Any]:
    """Upload a CSV file and return metadata with preview"""
    try:
        if not file_service.validate_file(file.filename):
            raise HTTPException(status_code=400, detail="Only CSV files are supported")
        
        session_id = str(uuid.uuid4())
        contents = await file.read()
        file_path = file_service.save_file(contents, session_id)
        
        df = file_service.load_dataframe(file_path)
        metadata = file_service.get_metadata(file.filename, df, session_id, file_path)
        
        session_data[session_id] = {
            "metadata": metadata,
            "dataframe": df
        }
        
        return {
            "success": True,
            "session_id": session_id,
            "filename": file.filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "preview": metadata["preview"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
