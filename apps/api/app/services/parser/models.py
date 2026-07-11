from pydantic import BaseModel


class WorkbookMetadata(BaseModel):
    """
    Lightweight workbook metadata extracted during upload.
    """

    sheet_count: int

    sheet_names: list[str]