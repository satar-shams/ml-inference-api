# ML Inference API

A production-oriented machine learning inference service built with **FastAPI**, **Docker**, structured logging, environment-based configuration, and automated testing.

The project focuses on the engineering practices required to serve machine learning models through a reliable and maintainable API, including separation of concerns, configuration management, containerization, security, observability, and reproducible execution.

The current implementation uses a lightweight dummy inference model to demonstrate the complete serving architecture. The inference component is designed to be replaced by a real ML model without changing the API layer.

---

## Overview

The service exposes machine learning inference through a clean HTTP API while keeping the API and inference layers separated.

### Project Goals

* Expose an ML model through a clean HTTP API
* Separate API handling from inference logic
* Apply practical Python backend engineering practices
* Provide structured request validation and error handling
* Support environment-based configuration
* Containerize the service with Docker
* Implement structured logging and health monitoring
* Prepare the service for cloud and container orchestration environments
* Keep the architecture flexible enough to replace the dummy model with a real ML model

---

## Architecture

The application is organized into separate responsibilities:

```text
Client Request
      │
      ▼
FastAPI API Layer
      │
      ▼
Input Validation
      │
      ▼
Inference Layer
      │
      ▼
Model Prediction
      │
      ▼
JSON Response
```

### API Layer

`app/api/main.py`

Responsible for:

* HTTP endpoints
* Request handling
* Pydantic validation
* HTTP error responses
* Calling the inference layer
* Returning structured JSON responses

### Inference Layer

`app/inference/model.py`

Responsible for:

* Model-related logic
* Prediction behavior
* Inference-related error handling
* Providing an independent interface for future ML models

This separation keeps the API independent from the underlying model implementation and makes the inference component easier to test and replace.

### Core Layer

`app/core/`

Contains shared application infrastructure:

* `config.py` — environment-based configuration
* `logger.py` — structured logging

---

## Features

* FastAPI REST API
* `/health` health-check endpoint
* `/predict` ML inference endpoint
* `/square_numbers` numerical processing endpoint
* Pydantic request validation
* Dummy ML inference model
* Separation of API and inference logic
* Structured JSON logging
* Environment-based configuration
* `.env` and `.env.example` support
* Docker containerization
* Non-root Docker execution
* Docker health checks
* Slim Python base image
* `.dockerignore` for cleaner images
* Automated API testing with Pytest
* Cloud and container-orchestration friendly architecture

---

## Technology Stack

### Backend

* Python 3.11
* FastAPI
* Pydantic
* Uvicorn

### Machine Learning

* Python-based inference architecture
* Modular model interface
* Dummy inference implementation

### Testing

* Pytest
* FastAPI TestClient
* HTTPX

### Deployment

* Docker
* Docker health checks
* Environment-based configuration

### Development

* Git
* Structured logging
* Configuration management
* CI/CD-compatible testing workflow

---

## API Endpoints

| Method | Endpoint          | Description                                        |
| ------ | ----------------- | -------------------------------------------------- |
| `GET`  | `/health`         | Returns the service health status                  |
| `POST` | `/predict`        | Receives input data and returns a model prediction |
| `POST` | `/square_numbers` | Returns squared values for provided numbers        |

### Health Check

**Request**

```http
GET /health
```

**Response**

```json
{
  "status": "healthy"
}
```

### Prediction

**Request**

```http
POST /predict
```

```json
{
  "text": "Hello"
}
```

**Response**

```json
{
  "input": "Hello",
  "prediction": "predicted(Hello)"
}
```

The current prediction logic is intentionally lightweight. The inference module is isolated so that a real machine learning model can be introduced without restructuring the API layer.

---

## Project Structure

```text
ml-inference-api/
├── app/
│   ├── api/
│   │   └── main.py          # FastAPI endpoints
│   ├── inference/
│   │   └── model.py         # Inference logic
│   └── core/
│       ├── config.py        # Environment configuration
│       └── logger.py        # Structured logging
├── tests/
├── Dockerfile
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
└── .dockerignore
```

---

## Running Locally

### 1. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```powershell
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the API

From the project root:

```bash
python -m app.api.main
```

The application loads configuration from `.env` through `python-dotenv`.

The server uses the configured host and port, with defaults of:

```text
0.0.0.0:8000
```

The API is then available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Docker

The application is packaged using a lightweight:

```text
python:3.11-slim
```

base image.

### Build the Image

From the project root:

```bash
docker build -t ml-inference-api .
```

### Run the Container

```bash
docker run --env-file .env -p 8000:8000 ml-inference-api
```

The API is available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

Health check:

```bash
curl http://localhost:8000/health
```

---

## Docker Engineering Practices

The container includes several production-oriented improvements.

### Slim Base Image

The project uses `python:3.11-slim` to reduce image size and unnecessary dependencies.

### Non-Root Execution

The container runs under a dedicated non-root user:

```dockerfile
RUN useradd -m appuser
USER appuser
```

This reduces the privileges available to the application inside the container.

### `.dockerignore`

The `.dockerignore` file prevents unnecessary and sensitive files from being copied into the image, including:

* `.git`
* `.env`
* `venv`
* `__pycache__`
* log files

### Health Check

The container includes a Docker health check based on the `/health` endpoint:

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
CMD curl --fail http://localhost:8000/health || exit 1
```

This allows Docker and compatible orchestration systems to detect an unhealthy service.

### Minimal System Dependencies

System packages are installed using:

```bash
apt-get install -y --no-install-recommends
```

The package cache is cleaned after installation to keep the final image smaller.

---

## Configuration

The application uses environment-based configuration instead of hardcoded runtime values.

Configuration is managed through:

```text
.env
.env.example
app/core/config.py
```

This allows configuration to be changed between development, testing, and deployment environments without modifying application code.

Sensitive configuration should remain outside version control.

---

## Logging

The application uses structured JSON logging.

Logs are written to standard output so they can be collected by Docker and other container runtimes.

Example:

```json
{
  "time": "2026-02-12 13:43:37",
  "level": "INFO",
  "message": "Prediction successful for input: string"
}
```

This approach makes application events easier to process in containerized and cloud environments.

---

## Testing

The project includes automated API testing.

The test suite covers the main service endpoints and uses FastAPI's `TestClient`.

Tests can be executed with:

```bash
python -m pytest -v
```

The testing setup also includes Windows-compatible asynchronous event-loop handling.

---

## Requirements

Production dependencies are defined in:

```text
requirements.txt
```

The current application uses:

```text
fastapi
uvicorn
pydantic
python-dotenv
```

Development and testing dependencies are maintained separately where applicable.

---

## Request Flow

The complete inference workflow is:

```text
Client
  │
  ▼
POST /predict
  │
  ▼
FastAPI
  │
  ▼
Pydantic Validation
  │
  ▼
Inference Module
  │
  ▼
Model Prediction
  │
  ▼
Structured JSON Response
```

Because the inference logic is isolated from the API layer, replacing the dummy model with an actual machine learning model can be done without changing the external API contract.

---

## Current Implementation

The project currently demonstrates:

* API design with FastAPI
* Separation of API and inference responsibilities
* Request validation with Pydantic
* Environment-based configuration
* Structured logging
* Automated testing
* Docker containerization
* Non-root container execution
* Docker health monitoring
* Production-oriented Python practices

The dummy inference implementation serves as a lightweight stand-in for a real ML model while preserving the architecture required for model serving.

---

## Project Status

The core inference-service architecture is implemented and containerized.

The project demonstrates an end-to-end workflow from:

**API Design → Inference Logic → Configuration → Logging → Testing → Dockerization → Health Monitoring**

The architecture is intentionally modular so that future model implementations can be integrated without restructuring the service.

---
