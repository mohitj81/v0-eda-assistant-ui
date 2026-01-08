def calculate_risk(profile):
    rows = profile["rows"]
    cols = profile["columns"]

    missing_values = sum(profile["missing"].values())
    duplicate_rows = profile["duplicates"]

    # Prevent division by zero
    total_cells = rows * cols if rows > 0 else 1

    missing_rate = missing_values / total_cells
    duplicate_rate = duplicate_rows / rows if rows > 0 else 0

    # Weighted risk formula
    risk_score = (missing_rate * 0.6) + (duplicate_rate * 0.4)

    # Risk level
    if risk_score < 0.3:
        level = "Low"
    elif risk_score < 0.6:
        level = "Medium"
    else:
        level = "High"

    # Issues
    issues = []
    if missing_rate > 0:
        issues.append(f"Missing values detected ({missing_rate:.2%})")
    if duplicate_rate > 0:
        issues.append(f"Duplicate rows detected ({duplicate_rate:.2%})")

    return {
        "risk_score": round(risk_score, 3),
        "risk_level": level,
        "issues": issues
    }
