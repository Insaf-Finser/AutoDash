from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Applications Settings"""

    APP_NAME: str = "InsightForge API"
    APP_VERSION: str = "0.1.0"

    HOST: str="0.0.0.0"
    PORT: int=8000

    DATABASE_URL: str

    REDIS_URL: str

    LOG_LEVEL: str = "INFO"

    UPLOAD_DIR: str = "uploads"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )
    
    
@lru_cache
def get_settings() -> Settings:
    return Settings()
    
    
settings = get_settings()