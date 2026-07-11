from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums import WorkbookStatus
from app.models import Workbook
from app.repositories.base_repository import BaseRepository


class WorkbookRepository(BaseRepository[Workbook]):

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        super().__init__(
            session=session,
            model=Workbook,
        )

    async def create(
        self,
        *,
        name: str,
        original_filename: str,
        stored_filename: str,
        storage_key: str,
        mime_type: str,
        file_extension: str,
        file_size: int,
        sheet_count:int,
        sheet_names:list[str]
    ) -> Workbook:

        workbook = Workbook(
            name=name,
            original_filename=original_filename,
            stored_filename=stored_filename,
            storage_key=storage_key,
            mime_type=mime_type,
            file_extension=file_extension,
            file_size=file_size,
            sheet_count=sheet_count,
            sheet_names=sheet_names,
            status=WorkbookStatus.UPLOADED,
        )

        self.session.add(workbook)

        await self.session.commit()

        await self.session.refresh(workbook)

        return workbook

    async def get_by_storage_key(
        self,
        storage_key: str,
    ) -> Workbook | None:

        result = await self.session.execute(
            select(Workbook).where(
                Workbook.storage_key == storage_key
            )
        )

        return result.scalar_one_or_none()      