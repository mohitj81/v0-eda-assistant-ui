def generate_cleaning_script(dataset_id: str):
    script = f"""
import pandas as pd

# Load dataset
df = pd.read_csv("backend/storage/uploaded/{dataset_id}.csv")

# Drop duplicate rows
df = df.drop_duplicates()

# Fill missing values
for col in df.columns:
    if df[col].dtype != 'object':
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# Save cleaned dataset
df.to_csv("backend/storage/cleaned/{dataset_id}_cleaned.csv", index=False)

print("Data cleaning successful! File saved to backend/storage/cleaned/")
"""

    return script
