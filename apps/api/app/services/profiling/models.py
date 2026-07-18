from pydantic import BaseModel


class ColumnProfile(BaseModel):
    name: str
    physical_type: str
    semantic_type: str
    confidence: float
    null_count: int
    unique_count: int


class WorksheetProfile(BaseModel):
    name: str
    row_count: int
    column_count: int
    columns: list[ColumnProfile]


class WorkbookProfile(BaseModel):
    worksheets: list[WorksheetProfile]