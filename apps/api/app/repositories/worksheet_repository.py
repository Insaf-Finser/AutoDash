from __future__ import annotations

from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Worksheet
from app.repositories.base_repository import BaseRepository


class WorksheetRepository(BaseRepository[Worksheet]):
    """
    Repository for worksheet persistence.
    """

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        super().__init__(
            session=session,
            model=Worksheet,
        )

    async def create_many(
        self,
        worksheets: Sequence[Worksheet],
    ) -> list[Worksheet]:

        self.session.add_all(worksheets)

        await self.session.commit()

        for worksheet in worksheets:
            await self.session.refresh(worksheet)

        return list(worksheets)

    async def list_by_workbook(
        self,
        workbook_id: UUID,
    ) -> list[Worksheet]:

        result = await self.session.execute(
            select(Worksheet)
            .where(
                Worksheet.workbook_id == workbook_id
            )
            .order_by(Worksheet.name)
        )

        return list(result.scalars().all())