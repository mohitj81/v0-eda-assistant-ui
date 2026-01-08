import json
from typing import Dict, Any
import anthropic

class AIService:
    def __init__(self, api_key: str = None):
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def generate_explanation(self, profile: Dict[str, Any], risk: Dict[str, Any]) -> str:
        """Generate AI-powered explanation for data issues"""
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
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
