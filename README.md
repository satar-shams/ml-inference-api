Quick Start (Windows-Friendly)

Follow these steps to run and test the ML Inference API locally and in Docker.

1️⃣ Clone & Setup
git clone https://github.com/satar-shams/ml-inference-api
cd ml-inference-api
python -m venv venv          # create virtual environment
venv\Scripts\activate        # activate venv (Windows)
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt   # dev dependencies (pytest, httpx)

2️⃣ Run Locally (Python)
python -m app.api.main


API: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Endpoints:

/health → returns {"status": "healthy"}

/predict → returns {"input": ..., "prediction": ...}

/square_numbers → returns squared numbers

3️⃣ Run in Docker
docker build -t ml-inference-api .
docker run --env-file .env -p 8000:8000 ml-inference-api


Health check: curl http://localhost:8000/health

Logs output to stdout (production-ready, Docker/K8s friendly)

4️⃣ Run Tests (Windows-Friendly)

Important: Stop any running Uvicorn server before testing.

Option 1 — Set PYTHONPATH

$env:PYTHONPATH = $PWD
pytest -v


Option 2 — Using python -m

python -m pytest -v


Notes:

Tests cover /health, /predict, and /square_numbers

Uses FastAPI TestClient

Windows async policy handled automatically in test files

Example Windows-Compatible Test Snippet:

import asyncio
import sys
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


✅ This ensures tests run smoothly on Windows, VSCode, or CI/CD pipelines.

5️⃣ Mentor-Ready Notes

All dependencies for production and development are in requirements.txt and requirements-dev.txt

Tests are isolated and don’t require the server to be running

Structured logging, .env config, and Docker best practices are already in place

This Quick Start section now allows anyone (Windows or Linux) to:

Set up the environment

Run the API locally or in Docker

Run tests without errors