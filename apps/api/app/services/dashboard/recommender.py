from __future__ import annotations

from uuid import uuid4

from app.services.dashboard.models import Chart, Dashboard
from app.services.dashboard.types import ChartType
from app.services.profiling.models import WorkbookProfile


class DashboardRecommender:
    """
    Generates chart recommendations from a WorkbookProfile.
    """

    def recommend(
        self,
        profile: WorkbookProfile,
    ) -> Dashboard:

        charts: list[Chart] = []

        for worksheet in profile.worksheets:
            print(f"\nWorksheet: {worksheet.name}")

            for column in worksheet.columns:
                print(column.name, "->", column.semantic_type)

        for worksheet in profile.worksheets:

            dates = []
            categories = []
            measures = []
            booleans = []

            # -----------------------------
            # Group columns
            # -----------------------------

            for column in worksheet.columns:

                if column.semantic_type == "date":
                    dates.append(column)

                elif column.semantic_type == "category":
                    categories.append(column)

                elif column.semantic_type == "measure":
                    measures.append(column)

                elif column.semantic_type == "boolean":
                    booleans.append(column)

            # -----------------------------
            # Rule 1
            # Date + Measure
            # -----------------------------

            for date in dates:
                for measure in measures:

                    charts.append(
                        Chart(
                            id=str(uuid4()),
                            worksheet=worksheet.name,
                            type=ChartType.LINE,
                            title=f"{measure.name} over {date.name}",
                            x=date.name,
                            y=measure.name,
                        )
                    )

            # -----------------------------
            # Rule 2
            # Category + Measure
            # -----------------------------

            for category in categories:
                for measure in measures:

                    charts.append(
                        Chart(
                            id=str(uuid4()),
                            worksheet=worksheet.name,
                            type=ChartType.BAR,
                            title=f"{measure.name} by {category.name}",
                            x=category.name,
                            y=measure.name,
                        )
                    )

            # -----------------------------
            # Rule 3
            # Boolean
            # -----------------------------

            for boolean in booleans:

                charts.append(
                    Chart(
                        id=str(uuid4()),
                        worksheet=worksheet.name,
                        type=ChartType.PIE,
                        title=f"{boolean.name} Distribution",
                        x=boolean.name,
                    )
                )

            # -----------------------------
            # Rule 4
            # KPI
            # -----------------------------

            for measure in measures:

                charts.append(
                    Chart(
                        id=str(uuid4()),
                        worksheet=worksheet.name,
                        type=ChartType.KPI,
                        title=f"Total {measure.name}",
                        y=measure.name,
                    )
                )

        return Dashboard(charts=charts)