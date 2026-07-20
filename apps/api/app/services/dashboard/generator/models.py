from pydantic import BaseModel


class WidgetLayout(BaseModel):
    x: int
    y: int
    w: int
    h: int


class WidgetConfig(BaseModel):
    """
    Configuration required to render a chart.
    """

    x: str | None = None
    y: str | None = None