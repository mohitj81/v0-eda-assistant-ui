from fastapi import APIRouter, HTTPException
from services.profiling_service import generate_profile
from services.risk_service import calculate_risk
import os

router = APIRouter(prefix="/risk", tags=["Risk Assessment"])

@router.get("/{dataset_id}")
async def get_risk(dataset_id: str):
    path = f"backend/storage/uploaded/{dataset_id}.csv"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Dataset not found")

    try:
        profile = generate_profile(path)
        risk = calculate_risk(profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Risk computation failed: {e}")

    return risk
