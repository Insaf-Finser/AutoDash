from pydantic import BaseModel
from app.services.dashboard.types import ChartType


class Chart(BaseModel):
    id: str
    type: ChartType

    title: str

    x: str | None = None
    y: str | None = None

    worksheet: str


class Dashboard(BaseModel):
    charts: list[Chart]