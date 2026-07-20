from __future__ import annotations

from app.services.profiler.detector import TypeDetector
from app.services.profiler.models import (
    ColumnProfile,
    WorkbookProfile,
    WorksheetProfile,
)
from app.services.profiler.statistics import StatisticsEngine
from app.services.profiler.semantic import SemanticDetector
from app.services.parser.models import Workbook



class Profiler:
    """
    Builds a complete profile of a workbook.
    """

    def __init__(self) -> None:
        self.detector = TypeDetector()
        self.statistics = StatisticsEngine()
        self.semantic = SemanticDetector()


    def profile(
        self,
        workbook: Workbook,
    ) -> WorkbookProfile:


        worksheets: list[WorksheetProfile] = []

        for worksheet in workbook.worksheets:

            dataframe = worksheet.data


            columns: list[ColumnProfile] = []

            for column_name in dataframe.columns:

                series = dataframe[column_name]

                physical_type = self.detector.detect(series)

                stats = self.statistics.profile(series)

                semantic_type, confidence = self.semantic.detect(
                    column_name=column_name,
                    physical_type=physical_type,
                    unique_count=stats.unique_count,
                    row_count=stats.row_count,
                    sample_values=stats.sample_values,
                )

                columns.append(
                    ColumnProfile(
                        name=column_name,
                        physical_type=physical_type,
                        semantic_type=semantic_type,
                        confidence=confidence,
                        row_count=stats.row_count,
                        null_count=stats.null_count,
                        unique_count=stats.unique_count,
                        unique_ratio=stats.unique_ratio,
                        sample_values=stats.sample_values,

                    )
                )

            worksheets.append(
                WorksheetProfile(
                    name=worksheet.name,
                    row_count=worksheet.row_count,
                    column_count=worksheet.column_count,
                    columns=columns,
                )
            )

        return WorkbookProfile(
            worksheets=worksheets,
        )