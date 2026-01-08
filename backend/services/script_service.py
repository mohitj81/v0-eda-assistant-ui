import pandas as pd
from typing import List

class ScriptService:
    @staticmethod
    def generate_cleaning_script(df: pd.DataFrame, profile: Dict[str, Any]) -> str:
        """Generate Python cleaning script"""
        script_lines = [
            "import pandas as pd",
            "import numpy as np",
            "",
            "# Load the dataset",
            "df = pd.read_csv('dataset.csv')",
            "",
            "print(f'Original shape: {df.shape}')",
            "print(f'Original duplicates: {df.duplicated().sum()}')",
            ""
        ]
        
        # Add missing value handling
        missing_cols = [col for col in profile["columns_analysis"] if col["missing_count"] > 0]
        if missing_cols:
            script_lines.append("# Handle missing values")
            for col in missing_cols:
                if pd.api.types.is_numeric_dtype(df[col["name"]]):
                    script_lines.append(f"df['{col['name']}'] = df['{col['name']}'].fillna(df['{col['name']}'].median())")
                else:
                    script_lines.append(f"df['{col['name']}'] = df['{col['name']}'].fillna(df['{col['name']}'].mode()[0] if not df['{col['name']}'].mode().empty else 'Unknown')")
            script_lines.append("")
        
        # Add duplicate removal
        script_lines.append("# Remove duplicates")
        script_lines.append("df = df.drop_duplicates()")
        script_lines.append("")
        
        # Add data type fixes
        script_lines.append("# Fix data types")
        for col in profile["columns_analysis"]:
            if col["dtype"] == "object":
                script_lines.append(f"# Column '{col['name']}' is currently {col['dtype']}")
                script_lines.append(f"# Verify and convert if needed: df['{col['name']}'] = pd.to_numeric(df['{col['name']}'], errors='coerce')")
        
        script_lines.append("")
        script_lines.append("# Save cleaned dataset")
        script_lines.append("df.to_csv('cleaned_dataset.csv', index=False)")
        script_lines.append("")
        script_lines.append("print(f'Cleaned shape: {df.shape}')")
        script_lines.append("print(f'Final duplicates: {df.duplicated().sum()}')")
        script_lines.append("print(f'Cleaned dataset saved as cleaned_dataset.csv')")
        
        return "\n".join(script_lines)
