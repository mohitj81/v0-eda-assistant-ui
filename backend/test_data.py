"""
Test data generation and validation script for EDA Assistant.
This script creates sample CSV files for testing all endpoints.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def create_test_datasets():
    """Create various test CSV files for testing."""
    
    test_dir = Path("test_data")
    test_dir.mkdir(exist_ok=True)
    
    # Dataset 1: Clean data
    df_clean = pd.DataFrame({
        'ID': range(1, 101),
        'Age': np.random.randint(18, 80, 100),
        'Income': np.random.randint(30000, 150000, 100),
        'Category': np.random.choice(['A', 'B', 'C'], 100),
        'Score': np.random.uniform(0, 100, 100)
    })
    df_clean.to_csv(test_dir / "clean_data.csv", index=False)
    print("Created: clean_data.csv")
    
    # Dataset 2: Data with missing values
    df_missing = df_clean.copy()
    df_missing.loc[np.random.choice(100, 10), 'Age'] = np.nan
    df_missing.loc[np.random.choice(100, 15), 'Income'] = np.nan
    df_missing.loc[np.random.choice(100, 5), 'Category'] = np.nan
    df_missing.to_csv(test_dir / "missing_data.csv", index=False)
    print("Created: missing_data.csv")
    
    # Dataset 3: Data with duplicates
    df_dupes = pd.concat([df_clean.head(10), df_clean], ignore_index=True)
    df_dupes.to_csv(test_dir / "duplicate_data.csv", index=False)
    print("Created: duplicate_data.csv")
    
    # Dataset 4: Messy data (realistic scenario)
    df_messy = df_clean.copy()
    # Add missing values
    df_messy.loc[np.random.choice(100, 12), 'Age'] = np.nan
    df_messy.loc[np.random.choice(100, 20), 'Income'] = np.nan
    # Add duplicates
    df_messy = pd.concat([df_messy, df_messy.sample(8)], ignore_index=True)
    # Add type inconsistencies
    df_messy.loc[5, 'Age'] = 'twenty'
    df_messy.loc[15, 'Income'] = 'high'
    df_messy.to_csv(test_dir / "messy_data.csv", index=False)
    print("Created: messy_data.csv")
    
    print(f"\nAll test datasets created in {test_dir}/")
    return test_dir

if __name__ == "__main__":
    create_test_datasets()
