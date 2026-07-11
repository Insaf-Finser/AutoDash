from __future__ import annotations

from uuid import uuid4

from fastapi import UploadFile

from app.repositories.workbook_repository import WorkbookRepository
from app.services.storage import StorageService
from app.services.parser import WorkbookParser

class WorkbookService:

    def __init__(
        self,
        repository: WorkbookRepository,
        storage: StorageService,
    ):
        self.repository = repository
        self.storage = storage
        self.parser = WorkbookParser()

    async def upload_workbook(
        self,
        *,
        filename:str,
        content_type: str,
        data: bytes,
    ):

        extension = filename.split(".")[-1]

        stored_filename = f"{uuid4()}.{extension}"

        object_key = await self.storage.save(
            stored_filename,
            data,
        )

        metadata = self.parser.extract_metadata(data)

        workbook = await self.repository.create(
            name=filename.rsplit(".", 1)[0],
            original_filename=filename,
            stored_filename=stored_filename,
            storage_key=object_key,
            mime_type=content_type,
            file_extension=f".{extension}",
            file_size=len(data),
            sheet_count=metadata.sheet_count,
            sheet_names=metadata.sheet_names,
        )

        return workbook