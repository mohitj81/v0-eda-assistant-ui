from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np
import os
import tempfile
import uuid
from datetime import datetime
from typing import Optional
import json
from pathlib import Path

# AI/LLM imports
import anthropic

app = FastAPI(title="EDA Assistant API", version="1.0.0")

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage for uploaded datasets
UPLOAD_DIR = tempfile.mkdtemp(prefix="eda_datasets_")
SESSION_DATA = {}  # In-memory storage for session data

client = anthropic.Anthropic()

# ============================================================================
# 1. POST /upload - File upload and validation
# ============================================================================

@app.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    """Upload a CSV file and return basic metadata"""
    try:
        # Validate file type
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are supported")
        
        # Generate session ID
        session_id = str(uuid.uuid4())
        
        # Save file
        file_path = os.path.join(UPLOAD_DIR, f"{session_id}.csv")
        contents = await file.read()
        with open(file_path, 'wb') as f:
            f.write(contents)
        
        # Read and validate CSV
        df = pd.read_csv(file_path)
        
        # Store metadata
        metadata = {
            "session_id": session_id,
            "filename": file.filename,
            "file_path": file_path,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "upload_time": datetime.now().isoformat(),
            "preview": df.head(5).to_dict(orient="records")
        }
        
        SESSION_DATA[session_id] = {
            "metadata": metadata,
            "dataframe": df
        }
        
        return {
            "success": True,
            "session_id": session_id,
            "filename": file.filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "preview": df.head(5).to_dict(orient="records")
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# 2. GET /profile - Real EDA profiling using pandas
# ============================================================================

@app.get("/profile")
async def get_profiling(session_id: str = Query(...)):
    """Perform real EDA profiling on the uploaded dataset"""
    try:
        if session_id not in SESSION_DATA:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = SESSION_DATA[session_id]["dataframe"]
        
        columns_analysis = []
        for col in df.columns:
            col_data = df[col]
            
            analysis = {
                "name": col,
                "dtype": str(col_data.dtype),
                "missing_count": int(col_data.isna().sum()),
                "missing_percentage": float((col_data.isna().sum() / len(df)) * 100),
                "unique_count": int(col_data.nunique()),
                "unique_percentage": float((col_data.nunique() / len(df)) * 100),
            }
            
            # Add statistical summary for numeric columns
            if pd.api.types.is_numeric_dtype(col_data):
                analysis.update({
                    "mean": float(col_data.mean()) if not col_data.isna().all() else None,
                    "median": float(col_data.median()) if not col_data.isna().all() else None,
                    "std": float(col_data.std()) if not col_data.isna().all() else None,
                    "min": float(col_data.min()) if not col_data.isna().all() else None,
                    "max": float(col_data.max()) if not col_data.isna().all() else None,
                })
            
            columns_analysis.append(analysis)
        
        # Overall statistics
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
        
        SESSION_DATA[session_id]["profile"] = profile
        return profile
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# 3. GET /risk - Real data quality risk scoring
# ============================================================================

@app.get("/risk")
async def get_risk_assessment(session_id: str = Query(...)):
    """Compute real data quality risk score"""
    try:
        if session_id not in SESSION_DATA:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = SESSION_DATA[session_id]["dataframe"]
        
        # Get profiling data if available
        if "profile" not in SESSION_DATA[session_id]:
            # Trigger profiling if not done
            await get_profiling(session_id)
        
        profile = SESSION_DATA[session_id]["profile"]
        
        # Missing value rate
        total_missing = sum(col["missing_count"] for col in profile["columns_analysis"])
        total_cells = profile["rows"] * profile["columns"]
        missing_rate = (total_missing / total_cells) if total_cells > 0 else 0
        
        # Duplicate rate
        duplicate_rate = profile["duplicate_percentage"] / 100
        
        # Datatype issue score (estimate based on mixed types)
        dtype_issue_score = 0.0
        non_numeric_cols = sum(1 for col in profile["columns_analysis"] if col["dtype"] == "object")
        if profile["columns"] > 0:
            dtype_issue_score = (non_numeric_cols / profile["columns"]) * 0.5
        
        risk_score = (missing_rate * 0.4) + (duplicate_rate * 0.3) + (dtype_issue_score * 0.3)
        
        # Determine risk level
        if risk_score > 0.6:
            risk_level = "High"
        elif risk_score > 0.3:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        # Identify critical issues
        issues = []
        
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
        
        risk_assessment = {
            "session_id": session_id,
            "risk_score": float(risk_score),
            "risk_level": risk_level,
            "components": {
                "missing_value_rate": float(missing_rate),
                "duplicate_rate": float(duplicate_rate),
                "datatype_issue_score": float(dtype_issue_score)
            },
            "issues": issues,
            "generated_at": datetime.now().isoformat()
        }
        
        SESSION_DATA[session_id]["risk"] = risk_assessment
        return risk_assessment
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# 4. GET /explain - AI-powered explanations using Claude
# ============================================================================

@app.get("/explain")
async def get_explanation(session_id: str = Query(...)):
    """Get AI-generated explanations for data issues"""
    try:
        if session_id not in SESSION_DATA:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Get profiling and risk data
        if "profile" not in SESSION_DATA[session_id]:
            await get_profiling(session_id)
        if "risk" not in SESSION_DATA[session_id]:
            await get_risk_assessment(session_id)
        
        profile = SESSION_DATA[session_id]["profile"]
        risk = SESSION_DATA[session_id]["risk"]
        
        prompt = f"""You are a data quality expert. Analyze this dataset profile and risk assessment:

Dataset Overview:
- Rows: {profile['rows']}
- Columns: {profile['columns']}
- Duplicates: {profile['duplicates']} ({profile['duplicate_percentage']:.1f}%)
- Memory Usage: {profile['memory_usage_mb']:.2f} MB

Risk Assessment:
- Risk Level: {risk['risk_level']}
- Risk Score: {risk['risk_score']:.2f}/1.0
- Missing Value Rate: {risk['components']['missing_value_rate']:.1%}
- Duplicate Rate: {risk['components']['duplicate_rate']:.1%}

Critical Issues:
{json.dumps([issue for issue in risk['issues'] if issue['severity'] == 'critical'], indent=2)}

Provide a concise analysis of these data quality issues and recommend specific data cleaning strategies. Focus on what columns need attention and why."""
        
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        explanation_text = message.content[0].text
        
        explanation = {
            "session_id": session_id,
            "explanation": explanation_text,
            "generated_at": datetime.now().isoformat()
        }
        
        SESSION_DATA[session_id]["explanation"] = explanation
        return explanation
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# 5. GET /script - Generate real Python cleaning script
# ============================================================================

@app.get("/script")
async def get_cleaning_script(session_id: str = Query(...)):
    """Generate real Python cleaning script"""
    try:
        if session_id not in SESSION_DATA:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df = SESSION_DATA[session_id]["dataframe"]
        profile = SESSION_DATA[session_id].get("profile")
        
        if not profile:
            await get_profiling(session_id)
            profile = SESSION_DATA[session_id]["profile"]
        
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
        
        # Add data type fixes for common issues
        script_lines.append("# Fix data types")
        for col in profile["columns_analysis"]:
            if col["dtype"] == "object":
                # Try to convert to numeric if appropriate
                script_lines.append(f"# Column '{col['name']}' is currently {col['dtype']}")
                script_lines.append(f"# Verify and convert if needed: df['{col['name']}'] = pd.to_numeric(df['{col['name']}'], errors='coerce')")
        
        script_lines.append("")
        script_lines.append("# Save cleaned dataset")
        script_lines.append("df.to_csv('cleaned_dataset.csv', index=False)")
        script_lines.append("")
        script_lines.append("print(f'Cleaned shape: {df.shape}')")
        script_lines.append("print(f'Final duplicates: {df.duplicated().sum()}')")
        script_lines.append("print(f'Cleaned dataset saved as cleaned_dataset.csv')")
        
        script = "\n".join(script_lines)
        
        response = {
            "session_id": session_id,
            "script": script,
            "generated_at": datetime.now().isoformat()
        }
        
        SESSION_DATA[session_id]["script"] = response
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# 6. GET /compare - Before/after comparison
# ============================================================================

@app.get("/compare")
async def get_comparison(session_id: str = Query(...)):
    """Compute before/after comparison of data cleaning"""
    try:
        if session_id not in SESSION_DATA:
            raise HTTPException(status_code=404, detail="Session not found")
        
        df_original = SESSION_DATA[session_id]["dataframe"]
        profile = SESSION_DATA[session_id].get("profile")
        
        if not profile:
            await get_profiling(session_id)
            profile = SESSION_DATA[session_id]["profile"]
        
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
        
        SESSION_DATA[session_id]["comparison"] = comparison
        return comparison
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Health check endpoint
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
