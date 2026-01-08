from pydantic import BaseModel
from typing import List

class RiskModel(BaseModel):
    risk_score: float
    risk_level: str
    issues: List[str]
