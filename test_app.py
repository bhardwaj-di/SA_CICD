# test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app  # Adjust the import based on your app structure

client = TestClient(app)

def test_predict_positive_sentiment():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "positive"}

def test_predict_negative_sentiment():
    response = client.post("/predict", json={"text": "I hate this!"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "negative"}

def test_predict_empty_input():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422  # Unprocessable Entity (Validation Error)

def test_predict_invalid_input():
    response = client.post("/predict", json={"wrong_key": "I love this!"})
    assert response.status_code == 422  # Unprocessable Entity (Validation Error)

if __name__ == "__main__":
    pytest.main()
