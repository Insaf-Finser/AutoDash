from enum import Enum


class ChartType(str, Enum):
    LINE = "line"
    BAR = "bar"
    PIE = "pie"
    KPI = "kpi"
    TABLE = "table"
    SCATTER = "scatter"
    HISTOGRAM = "histogram"