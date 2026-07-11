from __future__ import annotations

from io import BytesIO

from openpyxl import load_workbook

from app.services.parser.models import WorkbookMetadata


class WorkbookParser:
    """
    Extract workbook metadata.
    """

    def extract_metadata(
        self,
        data: bytes,
    ) -> WorkbookMetadata:

        workbook = load_workbook(
            filename=BytesIO(data),
            read_only=True,
            data_only=True,
        )

        sheet_names = workbook.sheetnames

        workbook.close()

        return WorkbookMetadata(
            sheet_count=len(sheet_names),
            sheet_names=sheet_names,
        )