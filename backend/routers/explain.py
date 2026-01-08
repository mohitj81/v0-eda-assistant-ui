from fastapi import APIRouter, Query, HTTPException
from typing import Dict, Any

router = APIRouter(prefix="/api", tags=["explain"])

ai_service = None
profiling_service = None
risk_service = None
session_data = None

@router.get("/explain")
async def get_explanation(session_id: str = Query(...)) -> Dict[str, Any]:
    """Get AI-powered explanation of data issues"""
    try:
        if session_id not in session_data:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = session_data[session_id]["dataframe"]
        
        # Ensure profile exists
        if "profile" not in session_data[session_id]:
            profile = profiling_service.profile_dataset(df, session_id)
            session_data[session_id]["profile"] = profile
        else:
            profile = session_data[session_id]["profile"]
        
        # Ensure risk exists
        if "risk" not in session_data[session_id]:
            risk_result = risk_service.calculate_risk_score(profile)
            issues = risk_service.identify_issues(profile)
            from datetime import datetime
            risk = {
                "risk_score": risk_result["risk_score"],
                "risk_level": risk_result["risk_level"],
                "components": risk_result["components"],
                "issues": issues,
                "generated_at": datetime.now().isoformat()
            }
            session_data[session_id]["risk"] = risk
        else:
            risk = session_data[session_id]["risk"]
        
        explanation_text = ai_service.generate_explanation(profile, risk)
        
        from datetime import datetime
        explanation = {
            "session_id": session_id,
            "explanation": explanation_text,
            "generated_at": datetime.now().isoformat()
        }
        
        session_data[session_id]["explanation"] = explanation
        return explanation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
