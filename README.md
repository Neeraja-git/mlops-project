# MLOps Project

## Overview
This project demonstrates an end-to-end MLOps pipeline:
- Trained ML model using scikit-learn
- Built API using FastAPI
- Containerized using Docker
- Automated CI/CD using GitHub Actions

## How to Run

### Run locally
uvicorn main:app --reload

### Run with Docker
docker build -t mlops-app .
docker run -p 8000:8000 mlops-app

## API Endpoint
/predict

## Tech Stack
- Python
- FastAPI
- Docker
- GitHub Actions
