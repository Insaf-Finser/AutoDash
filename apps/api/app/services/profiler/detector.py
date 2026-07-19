import polars as pl


class TypeDetector:

    def detect(self, series: pl.Series) -> str:
        dtype = series.dtype

        if dtype == pl.Int64:
            return "integer"

        if dtype == pl.Float64:
            return "float"

        if dtype == pl.Boolean:
            return "boolean"

        if dtype == pl.Date:
            return "date"

        if dtype == pl.Datetime:
            return "datetime"

        return "string"