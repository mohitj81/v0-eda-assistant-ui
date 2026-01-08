import os
from dotenv import load_dotenv
import google.genai as genai

# Load .env variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("ERROR: GEMINI_API_KEY missing in .env")

# Configure Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_ai_explanation(profile, risk):
    prompt = f"""
You are a professional data analyst.
Analyze the following dataset profile and risk assessment:

=== PROFILE ===
Rows: {profile['rows']}
Columns: {profile['columns']}
Missing Values: {profile['missing']}
Duplicates: {profile['duplicates']}
Data Types: {profile['dtypes']}
Unique Value Count: {profile['unique']}

=== RISK ===
Risk Score: {risk['risk_score']}
Risk Level: {risk['risk_level']}
Issues Found: {risk['issues']}

Provide a clear and simple explanation including:
- Summary
- Data issues
- Impact on ML models
- Recommended improvements
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt]   # IMPORTANT CHANGE
        )
        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
