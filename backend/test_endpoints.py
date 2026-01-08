"""
API endpoint testing guide for EDA Assistant Backend

## Prerequisites

1. Start the backend server:
   python main.py

2. Prepare a CSV file with your data

3. Test the endpoints using curl or requests

## Testing with cURL

### 1. Upload CSV
curl -X POST "http://localhost:8000/upload" \
  -F "file=@your_data.csv"

This returns a session_id. Save this for other tests.

### 2. Profile Data
curl "http://localhost:8000/profile?session_id=YOUR_SESSION_ID"

### 3. Risk Assessment
curl "http://localhost:8000/risk?session_id=YOUR_SESSION_ID"

### 4. AI Explanation
curl "http://localhost:8000/explain?session_id=YOUR_SESSION_ID"

### 5. Cleaning Script
curl "http://localhost:8000/script?session_id=YOUR_SESSION_ID"

### 6. Before/After Comparison
curl "http://localhost:8000/compare?session_id=YOUR_SESSION_ID"

## Testing with Python

import requests

# Upload
with open("your_data.csv", "rb") as f:
    response = requests.post("http://localhost:8000/upload", 
                           files={"file": f})
    session_id = response.json()["session_id"]

# Profile
response = requests.get(f"http://localhost:8000/profile?session_id={session_id}")
profile = response.json()

# And so on for other endpoints...

## Health Check

curl "http://localhost:8000/health"

## Notes

- All data processing is performed on YOUR uploaded CSV files
- No sample or dummy data is generated
- Sessions are stored in memory (cleared on server restart)
- Use the frontend UI at http://localhost:3000 for best experience

For API documentation, see backend/README.md
"""

print(__doc__)
