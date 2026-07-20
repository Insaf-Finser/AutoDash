from typing import Any

from pydantic import BaseModel

class ChartDataset(BaseModel):
    chart_id: str
    worksheet: str
    labels: list[Any]
    values: list[Any]

class DashboardData(BaseModel):
    datasets: list[ChartDataset]