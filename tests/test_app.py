import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route returns correct response."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "running"
    assert "message" in data
    assert data["version"] == "2.0.0"

def test_health_route(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

def test_version_route(client):
    """Test the new /version endpoint."""
    response = client.get("/version")
    assert response.status_code == 200
    data = response.get_json()
    assert data["version"] == "2.0.0"
    assert data["deployed_by"] == "Jenkins CI/CD"
    assert "timestamp" in data
