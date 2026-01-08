from fastapi import APIRouter, HTTPException
from services.profiling_service import generate_profile
from services.risk_service import calculate_risk
from services.ai_service import generate_ai_explanation
import os

router = APIRouter(prefix="/explain", tags=["AI Insights"])

@router.get("/{dataset_id}")
async def explain_dataset(dataset_id: str):
    path = f"backend/storage/uploaded/{dataset_id}.csv"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Dataset not found")

    try:
        profile = generate_profile(path)
        risk = calculate_risk(profile)
        explanation = generate_ai_explanation(profile, risk)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI explanation failed: {e}")

    return {"explanation": explanation}
