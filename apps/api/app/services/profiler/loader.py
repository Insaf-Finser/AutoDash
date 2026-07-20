from io import BytesIO

from app.services.parser.models import Workbook
from app.services.parser.models import Worksheet
import polars as pl


class WorkbookLoader:

    def load(self, data: bytes) -> Workbook:
        """
        Returns a dictionary of:
        {
            "Sheet1": DataFrame,
            "Sales": DataFrame,
        }
        """
        frames =  pl.read_excel(
            BytesIO(data),
            sheet_id=0,
        )

        worksheets: list[Worksheet] = []

        for sheet_name, dataframe in frames.items():
            worksheets.append(
                Worksheet(
                    name=sheet_name,
                    row_count=dataframe.height,
                    column_count=dataframe.width,
                    data=dataframe,
                )
            )

        return Workbook(
            worksheets=worksheets,
        )