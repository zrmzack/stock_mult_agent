import json
import logging

from fastapi.testclient import TestClient

from backend.app.core.logging import JsonFormatter
from backend.app.main import app


def test_json_formatter_includes_structured_extra_fields() -> None:
    formatter = JsonFormatter()
    record = logging.LogRecord(
        name="backend.request",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="request completed",
        args=(),
        exc_info=None,
    )
    record.request_id = "request-123"
    record.duration_ms = 42
    record.taskName = "Task-1"

    payload = json.loads(formatter.format(record))

    assert payload["message"] == "request completed"
    assert payload["logger"] == "backend.request"
    assert payload["request_id"] == "request-123"
    assert payload["duration_ms"] == 42
    assert "taskName" not in payload


def test_request_logging_adds_request_id_header() -> None:
    client = TestClient(app)

    response = client.get("/api/v1/health", headers={"x-request-id": "test-request"})

    assert response.status_code == 200
    assert response.headers["x-request-id"] == "test-request"
