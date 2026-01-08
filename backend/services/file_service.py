import os
import uuid
from pathlib import Path
import pandas as pd
from typing import Dict, Any, Tuple

class FileService:
    def __init__(self, upload_dir: str):
        self.upload_dir = upload_dir
        Path(upload_dir).mkdir(parents=True, exist_ok=True)
    
    def validate_file(self, filename: str) -> bool:
        """Validate that file is CSV"""
        return filename.endswith('.csv')
    
    def save_file(self, contents: bytes, session_id: str) -> str:
        """Save uploaded file and return path"""
        file_path = os.path.join(self.upload_dir, f"{session_id}.csv")
        with open(file_path, 'wb') as f:
            f.write(contents)
        return file_path
    
    def load_dataframe(self, file_path: str) -> pd.DataFrame:
        """Load CSV file as DataFrame"""
        return pd.read_csv(file_path)
    
    def get_preview(self, df: pd.DataFrame, rows: int = 5) -> list:
        """Get first N rows as preview"""
        return df.head(rows).to_dict(orient="records")
    
    def get_metadata(self, filename: str, df: pd.DataFrame, session_id: str, file_path: str) -> Dict[str, Any]:
        """Generate file metadata"""
        from datetime import datetime
        return {
            "session_id": session_id,
            "filename": filename,
            "file_path": file_path,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "upload_time": datetime.now().isoformat(),
            "preview": self.get_preview(df)
        }
