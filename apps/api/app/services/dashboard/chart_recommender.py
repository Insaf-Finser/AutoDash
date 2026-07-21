from __future__ import annotations

from uuid import uuid4

from app.services.dashboard.models import Chart, Dashboard
from app.services.dashboard.types import ChartType
from app.services.profiler.models import (
    ColumnProfile,
    WorkbookProfile,
    WorksheetProfile,
)
from app.enums.aggregation_type import AggregationType

from dataclasses import dataclass

@dataclass(slots=True)
class WorksheetContext:
    dates: list[ColumnProfile]
    categories: list[ColumnProfile]
    measures: list[ColumnProfile]
    booleans: list[ColumnProfile]

class ChartRecommender:
    def recommend(
        self,
        profile: WorkbookProfile,
    ) -> list[Chart]:

        charts: list[Chart] = []

        for worksheet in profile.worksheets:

            grouped = self._group_columns(worksheet)

            charts.extend(
                self._recommend_time_series(
                    worksheet,
                    grouped["dates"],
                    grouped["measures"],
                )
            )

            charts.extend(
                self._recommend_category_charts(
                    worksheet,
                    grouped["categories"],
                    grouped["measures"],
                )
            )

            charts.extend(
                self._recommend_boolean_charts(
                    worksheet,
                    grouped["booleans"],
                )
            )

            charts.extend(
                self._recommend_kpis(
                    worksheet,
                    grouped["measures"],
                )
            )

            charts.extend(
                self._recommend_scatter(
                    worksheet,
                    grouped["measures"],
                )
            )

            charts.extend(
                self._recommend_histograms(
                    worksheet,
                    grouped["measures"],
                )
            )

        return charts

    # ==========================================================
    # Helpers
    # ==========================================================

    def _group_columns(
        self,
        worksheet: WorksheetProfile,
    ) -> dict[str, list[ColumnProfile]]:

        grouped = {
            "dates": [],
            "categories": [],
            "measures": [],
            "booleans": [],
        }

        for column in worksheet.columns:

            match column.semantic_type:

                case "date":
                    grouped["dates"].append(column)

                case "category":
                    grouped["categories"].append(column)

                case "measure":
                    grouped["measures"].append(column)

                case "boolean":
                    grouped["booleans"].append(column)

        return grouped

    def _create_chart(
        self,
        *,
        worksheet: str,
        chart_type: ChartType,
        title: str,
        aggregation: AggregationType | None = None,
        x: str | None = None,
        y: str | None = None,
        
    ) -> Chart:

        return Chart(
            id=str(uuid4()),
            worksheet=worksheet,
            type=chart_type,
            title=title,
            aggregation=aggregation,
            x=x,
            y=y,

        )

    # ==========================================================
    # Recommendation Rules
    # ==========================================================

    def _recommend_time_series(
        self,
        worksheet: WorksheetProfile,
        dates: list[ColumnProfile],
        measures: list[ColumnProfile],
    ) -> list[Chart]:

        charts: list[Chart] = []

        if not dates or not measures:
            return charts

        for date in dates:
            for measure in measures:

                charts.append(
                    self._create_chart(
                        worksheet=worksheet.name,
                        chart_type=ChartType.LINE,
                        title=f"{measure.name} over {date.name}",
                        x=date.name,
                        y=measure.name,
                        aggregation=AggregationType.SUM,
                    )
                )

        return charts

    def _recommend_category_charts(
        self,
        worksheet: WorksheetProfile,
        categories: list[ColumnProfile],
        measures: list[ColumnProfile],
    ) -> list[Chart]:

        charts: list[Chart] = []

        if not categories or not measures:
            return charts

        for category in categories:
            for measure in measures:

                charts.append(
                    self._create_chart(
                        worksheet=worksheet.name,
                        chart_type=ChartType.BAR,
                        title=f"{measure.name} by {category.name}",
                        aggregation=AggregationType.SUM,
                        x=category.name,
                        y=measure.name,
                    )
                )

        return charts
    
    def _recommend_boolean_charts(
        self,
        worksheet: WorksheetProfile,
        booleans: list[ColumnProfile],
    ) -> list[Chart]:

        charts: list[Chart] = []

        if not booleans:
            return charts

        for boolean in booleans:

            charts.append(
                self._create_chart(
                    worksheet=worksheet.name,
                    chart_type=ChartType.PIE,
                    title=f"{boolean.name} Distribution",
                    aggregation=AggregationType.COUNT,
                    x=boolean.name,
                )
            )

        return charts

    def _recommend_kpis(
        self,
        worksheet: WorksheetProfile,
        measures: list[ColumnProfile],
    ) -> list[Chart]:

        charts: list[Chart] = []

        if not measures:
            return charts

        for measure in measures:

            charts.append(
                self._create_chart(
                    worksheet=worksheet.name,
                    chart_type=ChartType.KPI,
                    title=f"Total {measure.name}",
                    aggregation=AggregationType.SUM,
                    y=measure.name,
                )
            )

        return charts

    def _recommend_scatter(
        self,
        worksheet: WorksheetProfile,
        measures: list[ColumnProfile],
    ) -> list[Chart]:

        charts: list[Chart] = []

        if len(measures) < 2:
            return charts

        for i in range(len(measures)):
            for j in range(i + 1, len(measures)):

                charts.append(
                    self._create_chart(
                        worksheet=worksheet.name,
                        chart_type=ChartType.SCATTER,
                        title=f"{measures[i].name} vs {measures[j].name}",
                        aggregation=AggregationType.SUM,
                        x=measures[i].name,
                        y=measures[j].name,
                    )
                )

        return charts

    def _recommend_histograms(
        self,
        worksheet: WorksheetProfile,
        measures: list[ColumnProfile],
    ) -> list[Chart]:

        charts: list[Chart] = []

        for measure in measures:

            charts.append(
                self._create_chart(
                    worksheet=worksheet.name,
                    chart_type=ChartType.HISTOGRAM,
                    title=f"{measure.name} Distribution",
                    aggregation=AggregationType.COUNT,
                    x=measure.name,
                )
            )

        return charts