# EDA Assistant Backend API

FastAPI-based backend for Exploratory Data Analysis with real pandas processing, Claude AI integration, and automatic Python script generation.

## Features

- Real CSV file upload and validation
- Comprehensive data profiling with pandas
- Actual data quality risk scoring
- Claude AI-powered explanations
- Auto-generated Python cleaning scripts
- Before/after comparison metrics

## Quick Start

### 1. Install Dependencies

\`\`\`bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

### 2. Set Environment Variables

Create `.env` file:
\`\`\`
ANTHROPIC_API_KEY=your-api-key-here
\`\`\`

Get your free API key at: https://console.anthropic.com/

### 3. Run Server

\`\`\`bash
python main.py
\`\`\`

Server runs on `http://localhost:8000`

### 4. Test with cURL

\`\`\`bash
# Upload a CSV file
curl -X POST "http://localhost:8000/upload" \
  -F "file=@your-file.csv"

# Get profiling results (replace SESSION_ID)
curl "http://localhost:8000/profile?session_id=SESSION_ID"

# Get risk assessment
curl "http://localhost:8000/risk?session_id=SESSION_ID"

# Get AI explanation
curl "http://localhost:8000/explain?session_id=SESSION_ID"

# Get cleaning script
curl "http://localhost:8000/script?session_id=SESSION_ID"

# Get comparison
curl "http://localhost:8000/compare?session_id=SESSION_ID"
\`\`\`

## API Endpoints

### POST /upload
Upload CSV file and get metadata

**Request:** multipart/form-data with `file` field

**Response:**
\`\`\`json
{
  "success": true,
  "session_id": "uuid",
  "filename": "data.csv",
  "rows": 1000,
  "columns": 15,
  "column_names": ["col1", "col2", ...],
  "preview": [...]
}
\`\`\`

### GET /profile?session_id=uuid
Get comprehensive data profiling

**Response:**
\`\`\`json
{
  "session_id": "uuid",
  "rows": 1000,
  "columns": 15,
  "duplicates": 50,
  "duplicate_percentage": 5.0,
  "memory_usage_mb": 0.5,
  "columns_analysis": [
    {
      "name": "column_name",
      "dtype": "int64",
      "missing_count": 10,
      "missing_percentage": 1.0,
      "unique_count": 980,
      "unique_percentage": 98.0,
      "mean": 50.5,
      "median": 50,
      "std": 15.2,
      "min": 0,
      "max": 100
    }
  ],
  "generated_at": "2024-01-01T12:00:00"
}
\`\`\`

### GET /risk?session_id=uuid
Get data quality risk assessment

**Response:**
\`\`\`json
{
  "session_id": "uuid",
  "risk_score": 0.35,
  "risk_level": "Medium",
  "components": {
    "missing_value_rate": 0.02,
    "duplicate_rate": 0.05,
    "datatype_issue_score": 0.1
  },
  "issues": [
    {
      "severity": "warning",
      "type": "missing_values",
      "column": "age",
      "message": "Column 'age' has 5.2% missing values"
    }
  ],
  "generated_at": "2024-01-01T12:00:00"
}
\`\`\`

### GET /explain?session_id=uuid
Get AI-generated explanations using Claude

**Response:**
\`\`\`json
{
  "session_id": "uuid",
  "explanation": "Based on your dataset analysis...",
  "generated_at": "2024-01-01T12:00:00"
}
\`\`\`

### GET /script?session_id=uuid
Get auto-generated Python cleaning script

**Response:**
\`\`\`json
{
  "session_id": "uuid",
  "script": "import pandas as pd\nimport numpy as np\n\ndf = pd.read_csv('dataset.csv')\n...",
  "generated_at": "2024-01-01T12:00:00"
}
\`\`\`

### GET /compare?session_id=uuid
Get before/after comparison metrics

**Response:**
\`\`\`json
{
  "session_id": "uuid",
  "before": {
    "rows": 1000,
    "columns": 15,
    "missing_values": 50,
    "missing_percentage": 0.33,
    "duplicates": 30,
    "duplicate_percentage": 3.0,
    "memory_mb": 0.5
  },
  "after": {
    "rows": 970,
    "columns": 15,
    "missing_values": 0,
    "missing_percentage": 0.0,
    "duplicates": 0,
    "duplicate_percentage": 0.0,
    "memory_mb": 0.48
  },
  "improvements": {
    "rows_removed": 30,
    "missing_values_fixed": 50,
    "duplicates_removed": 30
  },
  "generated_at": "2024-01-01T12:00:00"
}
\`\`\`

### GET /health
Health check endpoint

**Response:**
\`\`\`json
{
  "status": "ok",
  "version": "1.0.0"
}
\`\`\`

## Development

### Run with auto-reload:
\`\`\`bash
pip install watchfiles
uvicorn main:app --reload
\`\`\`

### Run tests:
\`\`\`bash
# Create test CSV
python -c "
import pandas as pd
pd.DataFrame({
    'age': [25, 30, None, 45, 50],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'salary': [50000, 60000, 65000, 70000, 75000]
}).to_csv('test.csv', index=False)
"

# Test endpoints
curl -X POST "http://localhost:8000/upload" -F "file=@test.csv"
\`\`\`

## Production Deployment

### Using Gunicorn:
\`\`\`bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
\`\`\`

### Using Docker:
\`\`\`bash
docker build -t eda-assistant .
docker run -p 8000:8000 -e ANTHROPIC_API_KEY=your-key eda-assistant
\`\`\`

### Using Docker Compose:
\`\`\`bash
docker-compose up
\`\`\`

See DEPLOYMENT.md for detailed production setup.

## Session Management

Sessions are stored in memory. For production, implement database persistence.

## Error Handling

All endpoints return appropriate HTTP status codes:
- 200: Success
- 400: Bad request
- 404: Not found
- 500: Server error

## CORS Configuration

CORS is enabled for all origins in development. For production, restrict to your frontend domain:

\`\`\`python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
\`\`\`

## Support

For issues or questions, check:
1. API health: GET /health
2. Environment variables are set correctly
3. Backend and frontend are running
4. CORS is properly configured
