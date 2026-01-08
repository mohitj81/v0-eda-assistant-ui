from pydantic import BaseModel
from typing import Dict, Any

class ProfilingModel(BaseModel):
    rows: int
    columns: int
    missing: Dict[str, int]
    duplicates: int
    dtypes: Dict[str, str]
    unique: Dict[str, int]
    stats: Dict[str, Any]
