from fastapi import APIRouter, Query, HTTPException
from typing import Dict, Any

router = APIRouter(prefix="/api", tags=["compare"])

compare_service = None
session_data = None

@router.get("/compare")
async def get_comparison(session_id: str = Query(...)) -> Dict[str, Any]:
    """Get before/after comparison of data cleaning"""
    try:
        if session_id not in session_data:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df_original = session_data[session_id]["dataframe"]
        comparison = compare_service.compare_before_after(df_original, session_id)
        session_data[session_id]["comparison"] = comparison
        
        return comparison
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
