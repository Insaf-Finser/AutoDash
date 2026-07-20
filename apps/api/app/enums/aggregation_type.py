from enum import Enum


class AggregationType(str, Enum):
    SUM = "sum"
    COUNT = "count"
    AVERAGE = "average"
    MIN = "min"
    MAX = "max"