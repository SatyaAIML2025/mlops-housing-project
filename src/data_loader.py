from sklearn.datasets import fetch_california_housing
import pandas as pd
import os
from src.custom_exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

def load_and_save_data(data_dir="data/raw"):
    try:
        # Load dataset
        logger.info("Start fetching california housing data.")
        data = fetch_california_housing(as_frame=True)
        df = pd.concat([data.data, data.target.rename("MedHouseVal")], axis=1)
        # Save raw data
        os.makedirs(data_dir, exist_ok=True)
        logger.info("Directory created")
        df.to_csv(os.path.join(data_dir, "californ_housing.csv"), index=False)
        logger.info("Data saved to csv file")
        return df
    except Exception as e:
        logger.error(f"Error occurred while splitting data: {str(e)}")
        raise CustomException("Failed to splitting data") from e

if __name__ == "__main__":
    load_and_save_data()