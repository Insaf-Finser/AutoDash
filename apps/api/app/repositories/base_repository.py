from __future__ import annotations

from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Base repository for common CRUD operations.
    """

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ) -> None:
        self.session = session
        self.model = model

    async def get_by_id(
        self,
        entity_id: UUID,
    ) -> ModelType | None:
        result = await self.session.execute(
            select(self.model).where(
                self.model.id == entity_id
            )
        )

        return result.scalar_one_or_none()

    async def delete(
        self,
        entity: ModelType,
    ) -> None:
        await self.session.delete(entity)
        await self.session.commit()