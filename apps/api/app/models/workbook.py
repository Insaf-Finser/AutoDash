from __future__ import annotations

from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums import WorkbookStatus
from app.models.base import BaseModel




class Workbook(BaseModel):
    """
    Represents an uploaded Excel workbook.
    """

    __tablename__ = "workbooks"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    storage_key: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    file_extension: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    sheet_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        server_default="0",
        nullable=False,
    )

    status: Mapped[WorkbookStatus] = mapped_column(
        Enum(
            WorkbookStatus,
            name="workbook_status",
        ),
        default=WorkbookStatus.UPLOADED,
        server_default=WorkbookStatus.UPLOADED.name,
        nullable=False,
    )

    processed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    worksheets = relationship(
        "Worksheet",
        back_populates="workbook",
        cascade="all, delete-orphan",
    )