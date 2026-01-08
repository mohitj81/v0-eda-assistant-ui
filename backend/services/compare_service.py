import pandas as pd

def compare_before_after(before_path: str, after_path: str):
    """
    Compare original vs cleaned dataset and return differences.
    """

    before_df = pd.read_csv(before_path)
    after_df = pd.read_csv(after_path)

    result = {
        "before_shape": before_df.shape,
        "after_shape": after_df.shape,
        "rows_removed": before_df.shape[0] - after_df.shape[0],
        "columns": list(before_df.columns),
        "missing_before": int(before_df.isna().sum().sum()),
        "missing_after": int(after_df.isna().sum().sum()),
        "duplicates_before": int(before_df.duplicated().sum()),
        "duplicates_after": int(after_df.duplicated().sum())
    }

    return result
