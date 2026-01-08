from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ColumnAnalysis(BaseModel):
    name: str
    dtype: str
    missing_count: int
    missing_percentage: float
    unique_count: int
    unique_percentage: float
    mean: Optional[float] = None
    median: Optional[float] = None
    std: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None

class ProfilingResponse(BaseModel):
    session_id: str
    rows: int
    columns: int
    duplicates: int
    duplicate_percentage: float
    memory_usage_mb: float
    columns_analysis: List[ColumnAnalysis]
    generated_at: str
