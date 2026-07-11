from __future__ import annotations

from pathlib import Path

import aiofiles

from app.core.config import settings
from app.services.storage.base import StorageService


class LocalStorageService(StorageService):
    """
    Local filesystem storage implementation.
    """

    def __init__(self) -> None:
        self.root = Path(settings.LOCAL_STORAGE_PATH)

        self.workbooks = self.root / "workbooks"
        self.processed = self.root / "processed"
        self.exports = self.root / "exports"
        self.temp = self.root / "temp"

        self.workbooks.mkdir(parents=True, exist_ok=True)
        self.processed.mkdir(parents=True, exist_ok=True)
        self.exports.mkdir(parents=True, exist_ok=True)
        self.temp.mkdir(parents=True, exist_ok=True)

    async def save(
        self,
        file_name: str,
        data: bytes,
    ) -> str:

        object_key = f"workbooks/{file_name}"

        path = self.root / object_key

        async with aiofiles.open(path, "wb") as f:
            await f.write(data)

        return object_key

    async def read(
        self,
        object_key: str,
    ) -> bytes:

        path = self.root / object_key

        async with aiofiles.open(path, "rb") as f:
            return await f.read()

    async def delete(
        self,
        object_key: str,
    ) -> None:

        path = self.root / object_key

        if path.exists():
            path.unlink()

    async def exists(
        self,
        object_key: str,
    ) -> bool:

        return (self.root / object_key).exists()