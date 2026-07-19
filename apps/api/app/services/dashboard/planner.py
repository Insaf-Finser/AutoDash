from __future__ import annotations

from app.services.dashboard.models import Dashboard, DashboardPlan, Chart, LayoutItem
from app.services.dashboard.types import ChartType




class DashboardPlanner:
    """
    Generates a layout plan for a dashboard.

    Responsibilities:
        - Sort dashboard widgets
        - Decide widget sizes
        - Assign grid positions

    Does NOT:
        - Generate chart data
        - Render UI
        - Read Excel
    """

    GRID_COLUMNS = 12

    PRIORITY = {
        ChartType.KPI: 1,
        ChartType.LINE: 2,
        ChartType.BAR: 3,
        ChartType.PIE: 4,
        ChartType.SCATTER: 5,
        ChartType.HISTOGRAM: 6,
        ChartType.TABLE: 7,
    }

    SIZE_MAP = {
        ChartType.KPI: (3, 2),
        ChartType.LINE: (12, 5),
        ChartType.BAR: (6, 5),
        ChartType.PIE: (6, 5),
        ChartType.SCATTER: (6, 5),
        ChartType.HISTOGRAM: (6, 5),
        ChartType.TABLE: (12, 8),
    }

    def plan(
        self,
        dashboard: Dashboard,
    ) -> DashboardPlan:

        charts = self._sort_charts(dashboard)

        return self._place_flow_layout(charts)
    
    def _sort_charts(
        self,
        dashboard: Dashboard,
    ) -> list[Chart]:

        return sorted(
            dashboard.charts,
            key=self._get_priority,
        )
    
    def _get_size(
        self,
        chart: Chart,
    ) -> tuple[int, int]:

        try:
            return self.SIZE_MAP[chart.type]
        except KeyError:
            raise ValueError(f"Unsupported chart type: {chart.type}")
    
    def _place_flow_layout(
        self,
        charts: list[Chart],
    ) -> DashboardPlan:

        layout: list[LayoutItem] = []

        current_row = 0
        current_column = 0
        current_row_height = 0

        for chart in charts:

            width, height = self._get_size(chart)

            # Move to next row if widget doesn't fit
            if current_column + width > self.GRID_COLUMNS:
                current_row += current_row_height
                current_column = 0
                current_row_height = 0

            layout.append(
                LayoutItem(
                    chart_id=chart.id,
                    row=current_row,
                    column=current_column,
                    width=width,
                    height=height,
                )
            )

            current_column += width
            current_row_height = max(current_row_height, height)

        return DashboardPlan(charts=charts,layout=layout)

    def _get_priority(
        self,
        chart: Chart,
    ) -> int:
        return self.PRIORITY.get(chart.type, 999)