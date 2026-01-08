"""
Test script to validate all EDA Assistant API endpoints.
Run this after starting the backend server.
"""

import requests
import json
from pathlib import Path
import time

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health check endpoint."""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

def test_upload():
    """Test file upload endpoint."""
    print("\n=== Testing File Upload ===")
    
    # Create test file if not exists
    test_data_dir = Path("test_data")
    if not (test_data_dir / "messy_data.csv").exists():
        print("Creating test data...")
        import test_data
        test_data.create_test_datasets()
    
    # Upload file
    with open(test_data_dir / "messy_data.csv", "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/upload", files=files)
    
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response keys: {result.keys()}")
    
    if response.status_code == 200:
        print(f"Session ID: {result['session_id']}")
        print(f"Rows: {result['rows']}, Columns: {result['columns']}")
        return result['session_id']
    return None

def test_profile(session_id):
    """Test profiling endpoint."""
    print("\n=== Testing Profiling ===")
    response = requests.get(f"{BASE_URL}/profile?session_id={session_id}")
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Rows: {result['rows']}, Columns: {result['columns']}")
    print(f"Duplicates: {result['duplicates']}")
    print(f"Columns analyzed: {len(result['columns_analysis'])}")
    
    # Show first column analysis
    if result['columns_analysis']:
        col = result['columns_analysis'][0]
        print(f"  - {col['name']}: {col['dtype']}, Missing: {col['missing_percentage']:.1f}%")
    
    return response.status_code == 200

def test_risk(session_id):
    """Test risk assessment endpoint."""
    print("\n=== Testing Risk Assessment ===")
    response = requests.get(f"{BASE_URL}/risk?session_id={session_id}")
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Risk Level: {result['risk_level']}")
    print(f"Risk Score: {result['risk_score']:.2f}")
    print(f"Issues found: {len(result['issues'])}")
    
    for issue in result['issues'][:3]:
        print(f"  - [{issue['severity']}] {issue['message']}")
    
    return response.status_code == 200

def test_explanation(session_id):
    """Test AI explanation endpoint."""
    print("\n=== Testing AI Explanation ===")
    print("Calling Claude API (this may take a moment)...")
    
    response = requests.get(f"{BASE_URL}/explain?session_id={session_id}")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        explanation = result['explanation']
        print(f"Explanation length: {len(explanation)} characters")
        print(f"First 200 chars: {explanation[:200]}...")
    
    return response.status_code == 200

def test_script(session_id):
    """Test script generation endpoint."""
    print("\n=== Testing Script Generation ===")
    response = requests.get(f"{BASE_URL}/script?session_id={session_id}")
    print(f"Status: {response.status_code}")
    result = response.json()
    script = result['script']
    print(f"Script length: {len(script)} characters")
    print(f"Lines of code: {len(script.splitlines())}")
    print("Script preview:")
    print(script[:300])
    print("...")
    
    return response.status_code == 200

def test_comparison(session_id):
    """Test before/after comparison endpoint."""
    print("\n=== Testing Comparison ===")
    response = requests.get(f"{BASE_URL}/compare?session_id={session_id}")
    print(f"Status: {response.status_code}")
    result = response.json()
    
    print(f"Before - Rows: {result['before']['rows']}, Missing: {result['before']['missing_values']}")
    print(f"After  - Rows: {result['after']['rows']}, Missing: {result['after']['missing_values']}")
    print(f"Improvements:")
    print(f"  - Rows removed: {result['improvements']['rows_removed']}")
    print(f"  - Missing values fixed: {result['improvements']['missing_values_fixed']}")
    print(f"  - Duplicates removed: {result['improvements']['duplicates_removed']}")
    
    return response.status_code == 200

def run_all_tests():
    """Run all endpoint tests."""
    print("=" * 60)
    print("EDA Assistant API Test Suite")
    print("=" * 60)
    
    # Test health
    if not test_health():
        print("\nERROR: Backend is not running!")
        print("Start backend with: python main.py")
        return
    
    # Test upload
    session_id = test_upload()
    if not session_id:
        print("\nERROR: Upload failed!")
        return
    
    # Test remaining endpoints
    tests = [
        ("Profile", test_profile),
        ("Risk Assessment", test_risk),
        ("Explanation", test_explanation),
        ("Script Generation", test_script),
        ("Comparison", test_comparison),
    ]
    
    results = {}
    for name, test_func in tests:
        try:
            results[name] = test_func(session_id)
        except Exception as e:
            print(f"ERROR in {name}: {e}")
            results[name] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    for name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"{name}: {status}")
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    print(f"\nTotal: {passed}/{total} tests passed")

if __name__ == "__main__":
    run_all_tests()
