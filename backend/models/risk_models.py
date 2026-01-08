from pydantic import BaseModel
from typing import List, Dict, Any, Literal

class Issue(BaseModel):
    severity: Literal["critical", "warning", "info"]
    type: str
    column: Optional[str] = None
    message: str

class RiskComponents(BaseModel):
    missing_value_rate: float
    duplicate_rate: float
    datatype_issue_score: float

class RiskResponse(BaseModel):
    session_id: str
    risk_score: float
    risk_level: Literal["Low", "Medium", "High"]
    components: RiskComponents
    issues: List[Issue]
    generated_at: str
