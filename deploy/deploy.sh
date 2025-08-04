#!/bin/bash

echo "Pulling image from Docker Hub..."
docker pull <SatyaAIML2025>/housing-api:latest

echo "Running container on port 8000..."
docker run -d -p 8000:8000 --name housing-api <SatyaAIML2025>/housing-api:latest
