from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_version_endpoint():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.0.1"}
