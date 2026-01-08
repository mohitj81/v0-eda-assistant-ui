from fastapi import APIRouter, HTTPException
from services.compare_service import compare_before_after
import os

router = APIRouter(prefix="/compare", tags=["Before & After"])

@router.get("/{dataset_id}")
async def compare(dataset_id: str):
    raw_path = f"backend/storage/uploaded/{dataset_id}.csv"
    cleaned_path = f"backend/storage/cleaned/{dataset_id}_cleaned.csv"

    if not os.path.exists(raw_path):
        raise HTTPException(status_code=404, detail="Original dataset not found")

    if not os.path.exists(cleaned_path):
        raise HTTPException(status_code=404, detail="Cleaned dataset not found. Run script first.")

    try:
        result = compare_before_after(raw_path, cleaned_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison failed: {e}")

    return result
