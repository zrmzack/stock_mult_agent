from fastapi.testclient import TestClient

from backend.app.core.config import get_settings
from backend.app.main import app


client = TestClient(app)


def test_health_endpoint_returns_status_and_version() -> None:
    settings = get_settings()

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": settings.app_version,
    }


def test_version_endpoint_returns_app_metadata() -> None:
    settings = get_settings()

    response = client.get("/api/v1/version")

    assert response.status_code == 200
    assert response.json() == {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "api_prefix": settings.api_v1_prefix,
    }
