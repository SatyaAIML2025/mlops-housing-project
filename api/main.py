from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow
import mlflow.pyfunc

# Point to your MLflow Tracking server (where the registry is)
mlflow.set_tracking_uri("http://localhost:5000")

# ----------------------------
# Load model from MLflow Registry
# ----------------------------
MODEL_NAME = "BestHousingModel"
MODEL_VERSION = "latest"  # or e.g. "Production" stage

model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/{MODEL_VERSION}")

app = FastAPI(title="Housing Price Prediction API")


# Define input schema
class HousingInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
async def root():
    return {"message": "Housing Price Prediction API using MLflow Registry"}


@app.post("/predict")
async def predict_price(data: HousingInput):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)
    return {"predicted_price": float(pred[0])}
