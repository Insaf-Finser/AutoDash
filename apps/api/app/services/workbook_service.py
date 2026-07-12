from __future__ import annotations

from uuid import uuid4

from app.repositories.workbook_repository import WorkbookRepository
from app.repositories.worksheet_repository import WorksheetRepository
from app.services.storage import StorageService
from app.services.parser import WorkbookParser
from app.services.validation import WorkbookValidator

from app.models import Worksheet

class WorkbookService:

    def __init__(
        self,
        workbook_repository:WorkbookRepository,
        worksheet_repository:WorksheetRepository,
        storage: StorageService,
    ):
        self.workbook_repository = workbook_repository
        self.worksheet_repository = worksheet_repository
        self.storage = storage
        self.parser = WorkbookParser()
        self.validator=WorkbookValidator()

    async def upload_workbook(
        self,
        *,
        filename:str,
        content_type: str,
        data: bytes,
    ):

        extension = filename.rsplit(".", 1)[1]

        stored_filename = f"{uuid4()}.{extension}"

        

        self.validator.validate(
            filename=filename,
            data=data,
        )

        metadata = self.parser.extract_metadata(data)

        object_key = await self.storage.save(
            stored_filename,
            data,
        )

        workbook = await self.workbook_repository.create(
            name=filename.rsplit(".", 1)[0],
            original_filename=filename,
            stored_filename=stored_filename,
            storage_key=object_key,
            mime_type=content_type,
            file_extension=f".{extension}",
            file_size=len(data),
            sheet_count=metadata.sheet_count,
        )

        worksheets = []

        for sheet in metadata.worksheets:
            worksheets.append(
                Worksheet(
                    workbook_id = workbook.id,
                    name=sheet.name,
                    row_count=sheet.row_count,
                    column_count=sheet.column_count,
                )
            )

        await self.worksheet_repository.create_many(
            worksheets
        )

        return workbook 