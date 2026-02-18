from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_predict_with_text():
    payload = {"text": "Hello"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json() == {"input": "Hello", "prediction": "predicted(Hello)"}


def test_predict_with_default_text():
    payload = {}  # no "text" key
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "input" in data
    assert "prediction" in data
