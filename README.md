# MLOps Housing Project

This project demonstrates how to set up a machine learning pipeline with proper MLOps practices.

## Structure Part-1

- Dataset: California Housing
- Version control: Git & DVC
- Code: src/data_loader.py
- Preprocessing: notebooks/data_preprocessing.ipynb
- Model: src/model.py

## Model Training and Experiment Tracking Part-2

- Models Trained: LinearRegression, DecisionTreeRegressor
- Evaluation Metric: RMSE
- Experiment Tracking: MLflow
- Model Registry: Registered best model as `BestHousingModel`

## CI/CD Pipeline Part-3

- Built using **GitHub Actions**
- On push: runs **lint + tests**
- On success: builds Docker image and pushes to Docker Hub
- Deployment via shell script (`deploy/deploy.sh`)
