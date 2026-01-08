"""
Test data creation guide for EDA Assistant Backend

To test the API, you need to provide your own CSV files.
This script documents how to prepare test data.

## Testing with Your Own Data

1. Prepare a CSV file with your dataset
2. Use the upload endpoint:
   curl -X POST "http://localhost:8000/upload" -F "file=@your_data.csv"

3. Use the returned session_id for other endpoints:
   curl "http://localhost:8000/profile?session_id=YOUR_SESSION_ID"

## Example CSV Structure

Create a CSV file with headers and data:
id,name,age,salary,department
1,Alice,28,75000,Engineering
2,Bob,35,85000,Sales
3,Charlie,42,95000,Management
...

## Running Tests

Start the backend:
python main.py

In another terminal, run tests with your own data:
python test_endpoints.py

For more details, see README.md
"""

print(__doc__)
