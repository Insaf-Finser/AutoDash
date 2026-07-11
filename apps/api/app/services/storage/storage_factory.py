from app.core.config import settings
from app.services.storage.base import StorageService
from app.services.storage.local_storage import LocalStorageService


def get_storage_service() -> StorageService:
    """
    Return the configured storage implementation.
    """

    match settings.STORAGE_PROVIDER.lower():
        case "local":
            return LocalStorageService()

        case _:
            raise ValueError(
                f"Unsupported storage provider: {settings.STORAGE_PROVIDER}"
            )