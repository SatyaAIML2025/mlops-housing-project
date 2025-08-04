import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
import pandas as pd


def load_data(path="../data/raw/california_housing.csv"):
    df = pd.read_csv(path)
    X = df.drop(columns="MedHouseVal")
    y = df["MedHouseVal"]
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_and_log_model(model_name, model, X_train, X_test, y_train, y_test):
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        rmse = root_mean_squared_error(y_test, preds)

        mlflow.log_param("model", model_name)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(model, "model")

        print(f"{model_name} RMSE: {rmse:.4f}")
        return rmse
