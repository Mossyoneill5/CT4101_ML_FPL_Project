import pandas as pd

# Features selected from the data audit
features = ["minutes", "starts", "now_cost", "position", "team",
                "selected_by_percent", "cost_change_start"]
target = "total_points"

# Number and text columns in the features
num_cols = ["minutes", "starts", "now_cost", "selected_by_percent", "cost_change_start"]
cat_cols = ["position", "team"]

# Data dictionary details
conceptual_type = {
    "minutes": "numerical",
    "starts": "numerical",
    "now_cost": "numerical",
    "position": "nominal",
    "team": "nominal",
    "selected_by_percent": "numerical",
    "cost_change_start": "numerical",
    "total_points": "numerical",
}

units = {
    "minutes": "minutes",
    "starts": "matches",
    "now_cost": "£0.1m",
    "position": "label",
    "team": "name",
    "selected_by_percent": "%",
    "cost_change_start": "£0.1m",
    "total_points": "points",
}

availability = {
    "minutes": "yes",
    "starts": "yes",
    "now_cost": "yes",
    "position": "yes",
    "team": "yes",
    "selected_by_percent": "yes",
    "cost_change_start": "yes",
    "total_points": "n/a",
}

role = {
    "minutes": "input",
    "starts": "input",
    "now_cost": "input",
    "position": "input",
    "team": "input",
    "selected_by_percent": "input",
    "cost_change_start": "input",
    "total_points": "target",
}

    # Build a data disctionary describing each feature and the target
def data_dictionary(columns):
    return pd.DataFrame({
        "Conceptual Type": [conceptual_type[col] for col in columns],
        "Units": [units[col] for col in columns],
        "Role": [role[col] for col in columns],
        "Available at Prediction time": [availability[col] for col in columns]
        
    }, index=columns)