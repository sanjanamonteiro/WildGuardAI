
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "WildGuard AI backend is running"
    }


def test_health_endpoint():
    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["application"] == "WildGuard AI"
    assert data["message"] == "Backend API is operational"


def test_risk_map_endpoint():
    response = client.get("/api/risk-map")

    assert response.status_code == 200

    data = response.json()

    assert "total_cells" in data
    assert "crs" in data
    assert "data" in data
    assert data["crs"] == "EPSG:4326"
    assert data["total_cells"] == len(data["data"]["features"])


def test_wildlife_summary_endpoint():
    response = client.get("/api/wildlife-summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_observations" in data
    assert "unique_species" in data
    assert "class_distribution" in data
    assert "annual_observations" in data
    assert "data_warning" in data


def test_weather_summary_endpoint():
    response = client.get("/api/weather-summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_months" in data
    assert "latest_available_month" in data
    assert "monthly_records" in data
    assert data["total_months"] == len(data["monthly_records"])
