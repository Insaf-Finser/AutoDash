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

