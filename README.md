
ML Inference API (Production-Oriented)
Overview

This project demonstrates the design and implementation of a production-ready ML inference API.

The main goal is engineering quality and production readiness, not model accuracy.
A simple (dummy) inference logic is used initially and will be replaced or extended in later stages.

The service is built using FastAPI, containerized with Docker (later), and prepared for cloud deployment.

Project Goals

Expose an ML model (or dummy predictor) through a clean HTTP API

Apply real-world API design principles

Separate API logic from inference logic

Prepare the service for containerization and cloud deployment

Follow professional Python backend practices

Technology Stack (Current)

Python

FastAPI

Pydantic (request validation)

Uvicorn (ASGI server)

Planned:

Docker

Cloud deployment (AWS / GCP / Azure)

Logging, monitoring, and security

API Endpoints
GET /health

Health check endpoint used for service monitoring and orchestration.

Response

{
  "status": "healthy"
}

POST /predict

Dummy inference endpoint.

Request

{
  "text": "Hello"
}


Response

{
  "input": "Hello",
  "prediction": "dummy_result"
}


Note: Prediction logic is intentionally simple and will be separated into a dedicated inference module in later stages.


This structure supports:

separation of concerns

scalability

production readiness

Running the API Locally (Development)
1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
pip install fastapi uvicorn

3. Run the API from project root
uvicorn app.api.main:app --reload


The API will be available at:

http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

This setup is for local development only. Docker and cloud deployment will be added later.

Current Status

✅ System design and API specification completed

✅ API skeleton implemented with FastAPI

🚧 Inference logic separation

🚧 Dockerization

🚧 Cloud deployment

🚧 Security, logging, and monitoring

Notes

This project is developed incrementally following a daily execution plan.
The README will be updated as new components are added.

Why this README is correct now

Clear scope

Honest about current state

Professional run instructions

No premature complexity

Easy to extend later

This README is mentor-ready, GitHub-ready, and future-proof.

Next official step is Day 3 – Inference Logic Separation
Whenever you’re ready, we continue 🚀

🏗 Updated Project Structure
ml-inference-api/
├── app/
│   ├── api/
│   │   └── main.py          # FastAPI routes
│   ├── inference/
│   │   └── model.py         # Inference logic
│   └── core/
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md

🧠 Architecture Concept

The system is now divided into two clear layers:

1️⃣ API Layer (main.py)

Handles HTTP requests

Validates input using Pydantic

Calls inference module

Handles HTTP errors

Returns structured JSON responses

2️⃣ Inference Layer (model.py)

Contains model logic

Encapsulates prediction behavior

Handles inference-related errors

Independent from FastAPI or HTTP logic

🔁 Request Flow
Client Request
     ↓
FastAPI Endpoint (/predict)
     ↓
DummyModel.predict()
     ↓
Prediction Result
     ↓
JSON Response

📌 Example: model.py
class DummyModel:
    def __init__(self):
        pass

    def predict(self, text: str) -> str:
        try:
            result = f"predicted({text})"
            return result
        except Exception as e:
            raise RuntimeError(f"Inference error: {str(e)}")

📌 Example: API Usage

Request:

POST /predict
{
  "text": "Hello"
}


Response:

{
  "input": "Hello",
  "prediction": "predicted(Hello)"
}

✅ Why Separation of Concerns Matters

Improves maintainability

Makes inference logic testable independently

Allows easy replacement with real ML models

Keeps API layer clean

Follows production engineering standards

🚀 Production Readiness Improvement

The API no longer contains model logic directly.
This enables:

Easier scaling

Model swapping without changing endpoints

Clear responsibility boundaries


# ML Inference API – Step 4

Production-ready Python FastAPI project for ML inference.

---

## 📂 Project Structure

ml-inference-api/
├── app/
│ ├── api/
│ │ └── main.py # FastAPI endpoints
│ ├── inference/
│ │ └── model.py # Inference logic
│ └── core/
│ ├── config.py # Load environment variables
│ └── logger.py # Structured logging
├── tests/
├── Dockerfile
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
└── .dockerignore


---

## ⚡ Features

- FastAPI endpoints: `/health`, `/predict`, `/square_numbers`
- Dummy ML inference logic (`DummyModel`)  
- Structured JSON logging  
- Configurable via `.env` and `python-dotenv`  
- Environment-based defaults, no hardcoded values  
- Ready for Docker and cloud deployment  

---

## 🏃 How to Run Locally

### 1. Using Python `-m` (Recommended)

From **project root**:

```bash
python -m app.api.main
Automatically loads .env via python-dotenv

Starts Uvicorn server

Host/Port read from .env or defaults (0.0.0.0:8000)

2. Optional: Using PYTHONPATH (Professional)
export PYTHONPATH=$PWD
python ./app/api/main.py
Tells Python to treat the current folder as root

No code changes required

Useful if you have multiple nested packages

🐳 How to Run with Docker
Build image:

docker build -t ml-inference-api .
Run container:

docker run --env-file .env -p 8000:8000 ml-inference-api
Healthcheck endpoint:

curl http://localhost:8000/health
Professional Docker Notes:

WORKDIR /app sets root inside container

uvicorn app.api.main:app runs API directly

Logs are written to stdout, captured by Docker runtime

Environment variables can be overridden at runtime

🛠 Production-Ready Practices Implemented (Step 4)
Structured JSON logging (app/core/logger.py)

Error handling with proper HTTP responses

Environment-based configuration (.env + app/core/config.py)

Removed hardcoded values in API inputs and model logic

Separation of concerns:

app/api/main.py → API layer

app/inference/model.py → Inference layer

app/core/config.py → Configuration

app/core/logger.py → Logging

📦 Requirements
fastapi
uvicorn
pydantic
python-dotenv
✅ Step 4 Commit Notes
Day 4: Production-ready Python practices complete

Logging, env vars, removed hardcoded values

Ready for Docker and cloud deployment

main.py can run locally or in container without code changes


🎯 Goal

Containerize the FastAPI service to ensure consistent execution across environments.

🐳 Dockerfile

The application is packaged using a lightweight Python base image:

python:3.11-slim

Environment variables configured

Dependencies installed via requirements.txt

Uvicorn runs the API

Port 8000 exposed

🏗 Build Docker Image

From project root:

docker build -t ml-inference-api .

▶️ Run Container
docker run --env-file .env -p 8000:8000 ml-inference-api


--env-file .env → injects environment variables

-p 8000:8000 → maps container port to local machine

🌐 Access API

Open in browser:

http://localhost:8000/docs


Swagger UI confirms:

/health endpoint works

/predict endpoint works

OpenAPI schema loads correctly

📝 Logging

Structured JSON logging enabled

Logs output to stdout

Docker captures logs automatically

Compatible with production environments

Example log:

{
  "time": "2026-02-12 13:43:37",
  "level": "INFO",
  "message": "Prediction successful for input: string"
}

✅ Deliverables Completed

Dockerfile created

Image successfully built

Container running locally on Windows

API accessible via browser

Logging verified inside container

🏁 Day 5 Status: Completed

Designed the API (Day 1)

Structured the project (Day 2–3)

Added production-ready Python practices (Day 4)

Containerized the service (Day 5)
