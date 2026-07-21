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
from app.services.dashboard.chart_recommender import ChartRecommender
from dataclasses import dataclass

@dataclass(slots=True)
class WorksheetContext:
    dates: list[ColumnProfile]
    categories: list[ColumnProfile]
    measures: list[ColumnProfile]
    booleans: list[ColumnProfile]


class DashboardRecommender:
    """
    Rule-based dashboard recommendation engine.

    Responsibilities:
        - Analyze worksheet semantics
        - Recommend charts
        - Return a Dashboard

    Does NOT:
        - Parse Excel
        - Generate chart data
        - Render charts
    """

    def __init__(self):
        self.chart_recommender = ChartRecommender()

    def recommender(
            self,
            
    ) ->Dashboard:

        ranking = self.column_ranker.rank(worksheet)

        charts = self.chart_recommender.recommend(ranking)

        charts = self.chart_ranker.rank(charts)

        return Dashboard(charts=charts)