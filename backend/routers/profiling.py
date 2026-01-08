from fastapi import APIRouter, Query, HTTPException
from typing import Dict, Any

router = APIRouter(prefix="/api", tags=["profiling"])

profiling_service = None
session_data = None

@router.get("/profile")
async def get_profiling(session_id: str = Query(...)) -> Dict[str, Any]:
    """Get data profiling results"""
    try:
        if session_id not in session_data:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = session_data[session_id]["dataframe"]
        profile = profiling_service.profile_dataset(df, session_id)
        session_data[session_id]["profile"] = profile
        
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
