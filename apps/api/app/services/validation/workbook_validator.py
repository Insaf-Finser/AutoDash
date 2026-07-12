from pathlib import Path

from fastapi import HTTPException, status


class WorkbookValidator:
    """
    Validates uploaded workbook files.
    """

    ALLOWED_EXTENSIONS = {
        ".xlsx",
    }

    MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB

    def validate(
        self,
        *,
        filename: str,
        data: bytes,
    ) -> None:

        if not filename:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Filename is missing.",
            )

        extension = Path(filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported file type: {extension}",
            )

        if len(data) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty.",
            )

        if len(data) > self.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail="File exceeds maximum size.",
            )