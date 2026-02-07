import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_endpoint():
    """
    Test the health endpoint returns correct status
    """
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    assert "status" in data
    assert data["status"] in ["healthy", "unhealthy"]  # Could be unhealthy if DB not available