import pandas as pd
from typing import List, Dict, Any
from datetime import datetime

class RiskService:
    @staticmethod
    def calculate_risk_score(profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate data quality risk score"""
        # Missing value rate
        total_missing = sum(col["missing_count"] for col in profile["columns_analysis"])
        total_cells = profile["rows"] * profile["columns"]
        missing_rate = (total_missing / total_cells) if total_cells > 0 else 0
        
        # Duplicate rate
        duplicate_rate = profile["duplicate_percentage"] / 100
        
        # Datatype issue score
        dtype_issue_score = 0.0
        non_numeric_cols = sum(1 for col in profile["columns_analysis"] if col["dtype"] == "object")
        if profile["columns"] > 0:
            dtype_issue_score = (non_numeric_cols / profile["columns"]) * 0.5
        
        # Calculate risk score (40% missing, 30% duplicates, 30% datatype issues)
        risk_score = (missing_rate * 0.4) + (duplicate_rate * 0.3) + (dtype_issue_score * 0.3)
        
        # Determine risk level
        if risk_score > 0.6:
            risk_level = "High"
        elif risk_score > 0.3:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        return {
            "risk_score": float(risk_score),
            "risk_level": risk_level,
            "components": {
                "missing_value_rate": float(missing_rate),
                "duplicate_rate": float(duplicate_rate),
                "datatype_issue_score": float(dtype_issue_score)
            }
        }
    
    @staticmethod
    def identify_issues(profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify data quality issues"""
        issues = []
        
        # Check for high missing values
        for col in profile["columns_analysis"]:
            if col["missing_percentage"] > 50:
                issues.append({
                    "severity": "critical",
                    "type": "missing_values",
                    "column": col["name"],
                    "message": f"Column '{col['name']}' has {col['missing_percentage']:.1f}% missing values"
                })
            elif col["missing_percentage"] > 20:
                issues.append({
                    "severity": "warning",
                    "type": "missing_values",
                    "column": col["name"],
                    "message": f"Column '{col['name']}' has {col['missing_percentage']:.1f}% missing values"
                })
        
        # Check for duplicates
        if profile["duplicate_percentage"] > 10:
            issues.append({
                "severity": "critical",
                "type": "duplicates",
                "message": f"Dataset has {profile['duplicate_percentage']:.1f}% duplicate rows"
            })
        elif profile["duplicate_percentage"] > 5:
            issues.append({
                "severity": "warning",
                "type": "duplicates",
                "message": f"Dataset has {profile['duplicate_percentage']:.1f}% duplicate rows"
            })
        
        return issues
