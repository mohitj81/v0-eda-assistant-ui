# Backend Development Guide

## Local Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 4. Run Server with Auto-Reload
```bash
pip install watchfiles
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Testing

Use the frontend UI at \`http://localhost:3000\` or use cURL/Python requests to test endpoints.

See test_endpoints.py for examples.

## API Endpoints

- POST /upload - Upload CSV file
- GET /profile - Get data profiling
- GET /risk - Get risk assessment
- GET /explain - Get AI explanations
- GET /script - Get cleaning script
- GET /compare - Get before/after comparison
- GET /health - Health check

## Production

See README.md for deployment instructions.

## Debugging

Add debug logs:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Code Style

No specific formatting required, but follow PEP 8 conventions.
```bash
pip install black
black main.py
```
