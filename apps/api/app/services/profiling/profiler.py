from __future__ import annotations

from app.services.profiling.detector import TypeDetector
from app.services.profiling.loader import WorkbookLoader
from app.services.profiling.models import (
    ColumnProfile,
    WorkbookProfile,
    WorksheetProfile,
)
from app.services.profiling.statistics import StatisticsEngine
from app.services.profiling.semantic import SemanticDetector



class Profiler:
    """
    Builds a complete profile of a workbook.
    """

    def __init__(self) -> None:
        self.loader = WorkbookLoader()
        self.detector = TypeDetector()
        self.statistics = StatisticsEngine()
        self.semantic = SemanticDetector()


    def profile(
        self,
        data: bytes,
    ) -> WorkbookProfile:

        workbook = self.loader.load(data)

        worksheets: list[WorksheetProfile] = []

        for sheet_name, dataframe in workbook.items():

            columns: list[ColumnProfile] = []

            for column_name in dataframe.columns:

                series = dataframe[column_name]

                physical_type = self.detector.detect(series)

                stats = self.statistics.profile(series)

                columns.append(
                    ColumnProfile(
                        name=column_name,
                        physical_type=physical_type,
                        semantic_type=self.semantic.detect(
                            column_name,
                            physical_type,
                        ),
                        confidence=1.0,
                        null_count=stats["null_count"],
                        unique_count=stats["unique_count"],
                    )
                )

            worksheets.append(
                WorksheetProfile(
                    name=sheet_name,
                    row_count=dataframe.height,
                    column_count=dataframe.width,
                    columns=columns,
                )
            )

        return WorkbookProfile(
            worksheets=worksheets,
        )