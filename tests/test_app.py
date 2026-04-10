from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # The app serves the static `index.html` at `/`, so assert HTML response
    assert "<!DOCTYPE html>" in response.text
    assert "Mergington High School" in response.text