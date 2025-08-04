FROM python:3.11.7

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api ./api

# Set MLflow tracking endpoint if remote server is used (optional)
# ENV MLFLOW_TRACKING_URI=http://host.docker.internal:5000

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]