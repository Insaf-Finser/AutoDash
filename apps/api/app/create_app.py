from fastapi import FastAPI,Depends

from app.core.config import settings
from app.core.logging import configure_logging
from app.api.router import router

from app.database.session import get_db
from sqlalchemy import text

def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
    )
    app.include_router(router)

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