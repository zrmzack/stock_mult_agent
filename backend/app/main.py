from fastapi import FastAPI

from backend.app.api.v1.router import api_router
from backend.app.core.config import get_settings
from backend.app.core.logging import configure_logging
from backend.app.core.request_logging import request_logging_middleware


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    )
    application.middleware("http")(request_logging_middleware)
    application.include_router(api_router, prefix=settings.api_v1_prefix)
    return application


app = create_app()
