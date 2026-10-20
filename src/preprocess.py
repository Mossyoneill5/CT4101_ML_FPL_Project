import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# feature used to predict
feature_cols = ["minutes", "starts", "now_cost", "position", "team",
                "selected_by_percent", "cost_change_start"]
target_col = "total_points"

# Text categories and number columns in the features
num_cols = ["minutes", "starts", "now_cost", "selected_by_percent", "cost_change_start"]
cat_cols = ["position", "team"]


def prepare_data(df):
    # Drop players who have no minutes
    df = df[df["minutes"] > 0]
    X = df[feature_cols]
    y = df[target_col]
    return X, y


def build_preprocessor():
    # Number columns. Fill any empty values with the median
    num_pipe = make_pipeline(SimpleImputer(strategy="median"),
                             StandardScaler())

    # Categorical columns. Fill gaps with the most frequent value and one-hot encode
    cat_pipe = make_pipeline(SimpleImputer(strategy="most_frequent"),
                             OneHotEncoder(handle_unknown="ignore"))

    prep = ColumnTransformer([("num", num_pipe, num_cols),
                              ("cat", cat_pipe, cat_cols)])
    return prep