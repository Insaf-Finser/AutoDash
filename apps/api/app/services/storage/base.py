from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class StorageService(ABC):
    """
    Abstract storage interface.
    """

    @abstractmethod
    async def save(
        self,
        file_name: str,
        data: bytes,
    ) -> str:
        """
        Save a file.

        Returns
        -------
        object_key
        """
        raise NotImplementedError

    @abstractmethod
    async def read(
        self,
        object_key: str,
    ) -> bytes:
        raise NotImplementedError

    @abstractmethod
    async def delete(
        self,
        object_key: str,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def exists(
        self,
        object_key: str,
    ) -> bool:
        raise NotImplementedError