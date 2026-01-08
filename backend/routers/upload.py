from fastapi import APIRouter, UploadFile, HTTPException
from services.file_service import save_uploaded_file
import pandas as pd

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("")
async def upload_dataset(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    # Save file and return unique dataset ID + file path
    dataset_id, file_path = save_uploaded_file(file)

    # Read first 5 rows for preview
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read CSV: {e}")

    preview = df.head().to_dict(orient="records")

    return {
        "dataset_id": dataset_id,
        "preview": preview,
        "message": "File uploaded successfully"
    }
