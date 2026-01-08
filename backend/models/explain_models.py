from pydantic import BaseModel

class ExplanationResponse(BaseModel):
    session_id: str
    explanation: str
    generated_at: str
