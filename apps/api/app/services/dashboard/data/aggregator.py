

from app.enums import AggregationType

import polars as pl

from app.services.dashboard.models import Chart

class Aggregator:
    """
    Performs aggregations on extracted chart data.
    """

    def aggregate(
        self,
        data: pl.DataFrame,
        chart: Chart,
    )-> pl.DataFrame:
        match chart.aggregation:
            case AggregationType.SUM:
                return self._sum(data,chart)
            case AggregationType.COUNT:
                return self._count(data,chart)
            
        raise ValueError(f"Unsupported aggregation: {chart.aggregation}")
    
    def _sum(
            self,
            data: pl.DataFrame,
            chart:Chart
    )->pl.DataFrame:
        return (
            data
            .group_by(chart.x)
            .agg(
                pl.col(chart.y).sum().alias("value")
            ).sort(chart.x)
        )
    
    def _count(
        self,
        data: pl.DataFrame,
        chart: Chart,
    ) -> pl.DataFrame:

        if chart.x is None:
            # KPI: count all rows
            return pl.DataFrame({
                "value": [data.height],
            })

        # Group by the category and count rows
        return (
            data
            .group_by(chart.x)
            .len()
            .rename({"len": "value"})
            .sort(chart.x)
        )
