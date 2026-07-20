from pydantic import BaseModel


class WorksheetMetadata(BaseModel):
    name:str
    row_count:int
    column_count:int

class WorkbookMetadata(BaseModel):
    """
    Lightweight workbook metadata extracted during upload.
    """

    sheet_count: int

    worksheets: list[WorksheetMetadata]

from dataclasses import dataclass

import polars as pl


@dataclass(slots=True, frozen=True)
class Worksheet:
    name: str
    row_count: int
    column_count: int
    data: pl.DataFrame

@dataclass(slots=True, frozen=True)
class Workbook:
    worksheets: list[Worksheet]