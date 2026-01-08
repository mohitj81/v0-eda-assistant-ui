from fastapi import APIRouter, Query, HTTPException
from typing import Dict, Any

router = APIRouter(prefix="/api", tags=["risk"])

risk_service = None
profiling_service = None
session_data = None

@router.get("/risk")
async def get_risk(session_id: str = Query(...)) -> Dict[str, Any]:
    """Get data quality risk assessment"""
    try:
        if session_id not in session_data:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = session_data[session_id]["dataframe"]
        
        if "profile" not in session_data[session_id]:
            profile = profiling_service.profile_dataset(df, session_id)
            session_data[session_id]["profile"] = profile
        else:
            profile = session_data[session_id]["profile"]
        
        risk_result = risk_service.calculate_risk_score(profile)
        issues = risk_service.identify_issues(profile)
        
        from datetime import datetime
        risk_assessment = {
            "session_id": session_id,
            "risk_score": risk_result["risk_score"],
            "risk_level": risk_result["risk_level"],
            "components": risk_result["components"],
            "issues": issues,
            "generated_at": datetime.now().isoformat()
        }
        
        session_data[session_id]["risk"] = risk_assessment
        return risk_assessment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
