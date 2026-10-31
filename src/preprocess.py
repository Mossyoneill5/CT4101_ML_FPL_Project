from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from features import features, target, num_cols, cat_cols

def prepare_data(df):
    # Drop players who have no minutes
    df = df[df["minutes"] > 0]
    X = df[features]
    y = df[target]
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