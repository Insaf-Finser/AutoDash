from io import BytesIO

import polars as pl


class WorkbookLoader:

    def load(self, data: bytes) -> dict[str, pl.DataFrame]:
        """
        Returns a dictionary of:
        {
            "Sheet1": DataFrame,
            "Sales": DataFrame,
        }
        """
        return pl.read_excel(
            BytesIO(data),
            sheet_id=0,
        )