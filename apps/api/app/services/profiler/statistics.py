import polars as pl

from app.services.profiler.models import ColumnStatistics


class StatisticsEngine:

    def profile(self, series: pl.Series) -> ColumnStatistics:

        row_count = len(series)

        null_count = int(series.is_null().sum())

        unique_count = int(series.drop_nulls().n_unique())

        unique_ratio = unique_count / max(row_count, 1)

        sample_values = [
            str(v)
            for v in series.drop_nulls().head(5).to_list()
        ]

        return ColumnStatistics(
            row_count=row_count,
            null_count=null_count,
            unique_count=unique_count,
            unique_ratio=unique_ratio,
            sample_values=sample_values,
        )