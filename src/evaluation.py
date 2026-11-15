from sklearn.model_selection import KFold, cross_validate

def cv_model(model, X_train, y_train):

    # Use 5-fold cross-validation
    cv = KFold(n_splits=5, shuffle=True, random_state=42)

    # Evaluation metrics
    scoring = {
        "MAE": "neg_mean_absolute_error",
        "RMSE": "neg_root_mean_squared_error",
        "R2": "r2"
    }

    # Run cross-validation on the training data
    scores = cross_validate(model,X_train,y_train,cv=cv,scoring=scoring)

    # Return the evaluation results
    return {
        "MAE": -scores["test_MAE"],
        "RMSE": -scores["test_RMSE"],
        "R2": scores["test_R2"],
        "fit_time": scores["fit_time"],
        "score_time": scores["score_time"]
    } 