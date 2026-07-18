from pydantic import BaseModel


class ColumnProfile(BaseModel):
    # Basic Information
    name: str

    # Physical Analysis
    physical_type: str

    # Semantic Analysis
    semantic_type: str
    confidence: float = 1.0

    # Statistics
    row_count: int
    null_count: int
    unique_count: int
    unique_ratio: float

    # Sample Data
    sample_values: list[str]


class WorksheetProfile(BaseModel):
    name: str
    row_count: int
    column_count: int
    columns: list[ColumnProfile]


class WorkbookProfile(BaseModel):
    worksheets: list[WorksheetProfile]

class ColumnStatistics(BaseModel):
    row_count: int
    null_count: int
    unique_count: int
    unique_ratio: float
    sample_values: list[str]