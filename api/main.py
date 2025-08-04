from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow.pyfunc
import mlflow
import logging
from prometheus_fastapi_instrumentator import Instrumentator
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.db_logger import init_db, log_to_db


# ----------------------------
# Logging to file
# ----------------------------
logging.basicConfig(
    filename="prediction_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# Load model from MLflow Registry
# ----------------------------
mlflow.set_tracking_uri("http://localhost:5000")  # Update if remote
MODEL_NAME = "BestHousingModel"
MODEL_STAGE_OR_VERSION = "latest"
model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/{MODEL_STAGE_OR_VERSION}")

# ----------------------------
# FastAPI Setup
# ----------------------------
app = FastAPI(title="Housing Price Prediction API")
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Init SQLite DB
init_db()

# ----------------------------
# Input Schema
# ----------------------------
class HousingInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# ----------------------------
# Routes
# ----------------------------
@app.get("/")
async def root():
    return {"message": "Housing Price Prediction API using MLflow Registry"}

@app.post("/predict")
async def predict_price(data: HousingInput):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)
    predicted_price = float(pred[0])

    # Log to file
    logging.info(f"Input: {data.dict()} | Prediction: {predicted_price}")

    # Log to SQLite
    log_to_db(data.dict(), predicted_price)

    return {"predicted_price": predicted_price}
