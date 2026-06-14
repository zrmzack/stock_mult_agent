import logging
import time
from collections.abc import Awaitable, Callable
from uuid import uuid4

from fastapi import Request, Response


request_logger = logging.getLogger("backend.request")


async def request_logging_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    request_id = request.headers.get("x-request-id") or str(uuid4())
    start_time = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        duration_ms = _duration_ms(start_time)
        request_logger.exception(
            "request failed",
            extra={
                "request_id": request_id,
                "http_method": request.method,
                "path": request.url.path,
                "client_host": _client_host(request),
                "duration_ms": duration_ms,
            },
        )
        raise

    duration_ms = _duration_ms(start_time)
    response.headers["x-request-id"] = request_id
    request_logger.info(
        "request completed",
        extra={
            "request_id": request_id,
            "http_method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "client_host": _client_host(request),
            "duration_ms": duration_ms,
        },
    )
    return response


def _duration_ms(start_time: float) -> int:
    return round((time.perf_counter() - start_time) * 1000)


def _client_host(request: Request) -> str | None:
    if request.client is None:
        return None
    return request.client.host
