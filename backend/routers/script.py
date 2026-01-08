from fastapi import APIRouter, Query, HTTPException
from typing import Dict, Any

router = APIRouter(prefix="/api", tags=["script"])

script_service = None
profiling_service = None
session_data = None

@router.get("/script")
async def get_script(session_id: str = Query(...)) -> Dict[str, Any]:
    """Get Python cleaning script"""
    try:
        if session_id not in session_data:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = session_data[session_id]["dataframe"]
        
        if "profile" not in session_data[session_id]:
            profile = profiling_service.profile_dataset(df, session_id)
            session_data[session_id]["profile"] = profile
        else:
            profile = session_data[session_id]["profile"]
        
        script = script_service.generate_cleaning_script(df, profile)
        
        from datetime import datetime
        response = {
            "session_id": session_id,
            "script": script,
            "generated_at": datetime.now().isoformat()
        }
        
        session_data[session_id]["script"] = response
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
