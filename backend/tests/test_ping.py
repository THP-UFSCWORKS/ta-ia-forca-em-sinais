from fastapi.testclient import TestClient
from app.core.config import create_app

client = TestClient(create_app())

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "pong"}