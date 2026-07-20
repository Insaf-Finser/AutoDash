from app.models.workbook import Workbook
from app.services.dashboard.data.models import DashboardData,  ChartDataset
from app.services.dashboard.models import Chart, DashboardPlan
from app.models.worksheet import Worksheet
from app.services.dashboard.data.aggregator import Aggregator

from app.services.dashboard.types import ChartType
import polars as pl


class ChartDataEngine:
    """
    Computes the datasets required to render a dashboard.
    """

    def __init__(self):
        self._aggregator = Aggregator()

    def build(
        self,
        workbook: Workbook,
        plan: DashboardPlan,
    ) -> DashboardData:
        """
        Compute datasets for every chart in the dashboard.
        """
        datasets = []

        for chart in plan.charts:
            dataset = self._build_dataset(workbook, chart)
            datasets.append(dataset)
        
        return DashboardData(
            datasets=datasets,
        )
    
    def _build_dataset(
        self,
        workbook: Workbook,
        chart: Chart,
    ) -> ChartDataset:
        worksheet = self._get_worksheet(workbook=workbook,chart=chart)
        data = self._extract_data(worksheet,chart)
        aggregated = self._aggregate_data(data,chart)
        return self._create_dataset(chart, aggregated)
    
    def _get_worksheet(
        self,
        workbook: Workbook,
        chart: Chart,
    ) -> Worksheet:

        for worksheet in workbook.worksheets:
            if worksheet.name == chart.worksheet:
                return worksheet

        raise ValueError(
            f"Worksheet '{chart.worksheet}' not found."
        )

    def _extract_data(
        self,
        worksheet: Worksheet,
        chart: Chart,
    ) -> pl.DataFrame:
        """
        Extract the columns required by a chart.
        """
        columns = []

        if chart.x is not None:
            columns.append(chart.x)

        if chart.y is not None:
            columns.append(chart.y)

        return worksheet.data.select(columns)
    
    def _aggregate_data(
        self,
        data: pl.DataFrame,
        chart: Chart,
    ) -> pl.DataFrame:
        """
        Aggregate extracted data into labels and values.
        """
        return self._aggregator.aggregate(data,chart)
    
    def _create_dataset(
        self,
        chart: Chart,
        data: pl.DataFrame,
    ) -> ChartDataset:

        if chart.type == ChartType.KPI:
            return ChartDataset(
                chart_id=chart.id,
                worksheet=chart.worksheet,
                labels=["Total"],
                values=data.get_column("value").to_list(),
            )

        labels = data.get_column(chart.x).to_list()
        values = data.get_column("value").to_list()

        return ChartDataset(
            chart_id=chart.id,
            worksheet=chart.worksheet,
            labels=labels,
            values=values,
        )