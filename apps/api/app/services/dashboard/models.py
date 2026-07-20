from pydantic import BaseModel
from app.services.dashboard.types import ChartType
from app.enums.aggregation_type import AggregationType


class Chart(BaseModel):
    id: str
    type: ChartType

    title: str

    x: str | None = None
    y: str | None = None

    worksheet: str

    aggregation: AggregationType | None = None


class Dashboard(BaseModel):
    charts: list[Chart]


class LayoutItem(BaseModel):
    chart_id: str

    row: int
    column: int

    width: int
    height: int

class DashboardPlan(BaseModel):
    charts: list[Chart]
    layout: list[LayoutItem]