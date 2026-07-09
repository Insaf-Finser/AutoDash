from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
    )

    @app.get("/")
    async def root():
        return {
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "status": "running",
        }

    @app.get("/health")
    async def health():
        return {
            "status": "healthy",
        }

    return app