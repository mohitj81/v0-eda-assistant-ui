from fastapi import APIRouter, HTTPException
from services.profiling_service import generate_profile
import os

router = APIRouter(prefix="/profile", tags=["Profiling"])

@router.get("/{dataset_id}")
async def get_profile(dataset_id: str):
    path = f"backend/storage/uploaded/{dataset_id}.csv"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Dataset not found")

    try:
        profile = generate_profile(path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Profiling failed: {e}")

    return profile
