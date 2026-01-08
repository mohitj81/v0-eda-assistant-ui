import pandas as pd

def generate_profile(path: str):
    df = pd.read_csv(path)

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "unique": {col: df[col].nunique() for col in df.columns},
        "stats": df.describe(include="all").fillna("").to_dict(),
    }

    return summary
