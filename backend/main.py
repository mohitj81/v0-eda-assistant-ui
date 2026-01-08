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

from services.file_service import FileService
from services.profiling_service import ProfilingService
from services.risk_service import RiskService
from services.ai_service import AIService
from services.script_service import ScriptService
from services.compare_service import CompareService

from routers import upload, profiling, risk, explain, script, compare

app = FastAPI(
    title="EDA Assistant API",
    version="1.0.0",
    description="Production-ready backend for exploratory data analysis with real pandas processing"
)

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

file_service = FileService(UPLOAD_DIR)
profiling_service = ProfilingService()
risk_service = RiskService()
ai_service = AIService()
script_service = ScriptService()
compare_service = CompareService()

upload.file_service = file_service
upload.session_data = SESSION_DATA

profiling.profiling_service = profiling_service
profiling.session_data = SESSION_DATA

risk.risk_service = risk_service
risk.profiling_service = profiling_service
risk.session_data = SESSION_DATA

explain.ai_service = ai_service
explain.profiling_service = profiling_service
explain.risk_service = risk_service
explain.session_data = SESSION_DATA

script.script_service = script_service
script.profiling_service = profiling_service
script.session_data = SESSION_DATA

compare.compare_service = compare_service
compare.session_data = SESSION_DATA

app.include_router(upload.router)
app.include_router(profiling.router)
app.include_router(risk.router)
app.include_router(explain.router)
app.include_router(script.router)
app.include_router(compare.router)

# ============================================================================
# Health check endpoint
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
