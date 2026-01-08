from pydantic import BaseModel

class ExplainModel(BaseModel):
    explanation: str
