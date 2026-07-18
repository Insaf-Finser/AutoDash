import polars as pl


class StatisticsEngine:

    def profile(self, series: pl.Series) -> dict:
        return {
            "null_count": series.null_count(),
            "unique_count": series.n_unique(),
        }