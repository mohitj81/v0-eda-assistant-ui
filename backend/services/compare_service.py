import pandas as pd
from typing import Dict, Any

class CompareService:
    @staticmethod
    def compare_before_after(df_original: pd.DataFrame, session_id: str) -> Dict[str, Any]:
        """Compare before and after cleaning"""
        df_cleaned = df_original.copy()
        
        # Remove duplicates
        df_cleaned = df_cleaned.drop_duplicates()
        
        # Handle missing values
        for col in df_cleaned.columns:
            if df_cleaned[col].isna().any():
                if pd.api.types.is_numeric_dtype(df_cleaned[col]):
                    df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
                else:
                    mode_val = df_cleaned[col].mode()
                    if not mode_val.empty:
                        df_cleaned[col] = df_cleaned[col].fillna(mode_val[0])
        
        # Calculate metrics
        missing_before = df_original.isna().sum().sum()
        missing_after = df_cleaned.isna().sum().sum()
        
        duplicates_before = df_original.duplicated().sum()
        duplicates_after = df_cleaned.duplicated().sum()
        
        from datetime import datetime
        comparison = {
            "session_id": session_id,
            "before": {
                "rows": len(df_original),
                "columns": len(df_original.columns),
                "missing_values": int(missing_before),
                "missing_percentage": float((missing_before / (len(df_original) * len(df_original.columns))) * 100),
                "duplicates": int(duplicates_before),
                "duplicate_percentage": float((duplicates_before / len(df_original)) * 100),
                "memory_mb": float(df_original.memory_usage(deep=True).sum() / 1024 / 1024)
            },
            "after": {
                "rows": len(df_cleaned),
                "columns": len(df_cleaned.columns),
                "missing_values": int(missing_after),
                "missing_percentage": float((missing_after / (len(df_cleaned) * len(df_cleaned.columns))) * 100) if len(df_cleaned) > 0 else 0,
                "duplicates": int(duplicates_after),
                "duplicate_percentage": float((duplicates_after / len(df_cleaned)) * 100) if len(df_cleaned) > 0 else 0,
                "memory_mb": float(df_cleaned.memory_usage(deep=True).sum() / 1024 / 1024)
            },
            "improvements": {
                "rows_removed": len(df_original) - len(df_cleaned),
                "missing_values_fixed": int(missing_before - missing_after),
                "duplicates_removed": int(duplicates_before - duplicates_after)
            },
            "generated_at": datetime.now().isoformat()
        }
        
        return comparison
