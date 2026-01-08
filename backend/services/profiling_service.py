import pandas as pd
from typing import List, Dict, Any
from datetime import datetime

class ProfilingService:
    @staticmethod
    def analyze_column(col_name: str, col_data: pd.Series, df_len: int) -> Dict[str, Any]:
        """Analyze a single column"""
        analysis = {
            "name": col_name,
            "dtype": str(col_data.dtype),
            "missing_count": int(col_data.isna().sum()),
            "missing_percentage": float((col_data.isna().sum() / df_len) * 100),
            "unique_count": int(col_data.nunique()),
            "unique_percentage": float((col_data.nunique() / df_len) * 100),
        }
        
        # Add statistics for numeric columns
        if pd.api.types.is_numeric_dtype(col_data):
            if not col_data.isna().all():
                analysis.update({
                    "mean": float(col_data.mean()),
                    "median": float(col_data.median()),
                    "std": float(col_data.std()),
                    "min": float(col_data.min()),
                    "max": float(col_data.max()),
                })
            else:
                analysis.update({
                    "mean": None,
                    "median": None,
                    "std": None,
                    "min": None,
                    "max": None,
                })
        
        return analysis
    
    @staticmethod
    def profile_dataset(df: pd.DataFrame, session_id: str) -> Dict[str, Any]:
        """Run full profiling on dataset"""
        columns_analysis = []
        for col in df.columns:
            col_analysis = ProfilingService.analyze_column(col, df[col], len(df))
            columns_analysis.append(col_analysis)
        
        profile = {
            "session_id": session_id,
            "rows": len(df),
            "columns": len(df.columns),
            "duplicates": int(df.duplicated().sum()),
            "duplicate_percentage": float((df.duplicated().sum() / len(df)) * 100),
            "memory_usage_mb": float(df.memory_usage(deep=True).sum() / 1024 / 1024),
            "columns_analysis": columns_analysis,
            "generated_at": datetime.now().isoformat()
        }
        
        return profile
