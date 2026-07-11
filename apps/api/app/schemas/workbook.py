from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.enums import WorkbookStatus


class WorkbookResponse(BaseModel):
    id: UUID

    name: str

    original_filename: str

    file_size: int

    sheet_count: int

    status: WorkbookStatus

    created_at: datetime

    model_config = {
        "from_attributes": True,
    }