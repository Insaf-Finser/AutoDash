from app.services.dashboard.data.models import DashboardData
from app.services.dashboard.recommender import DashboardRecommender
from app.services.profiler.models import WorkbookProfile
from app.services.dashboard.data.engine import ChartDataEngine
from app.services.dashboard.planner import DashboardPlanner
from app.models.workbook import Workbook

class DashboardGenerator:
    """
    Generates a dashboard from a workbook profile.
    """

    def __init__(self):
        self.recommender = DashboardRecommender()
        self.planner = DashboardPlanner()
        self.engine = ChartDataEngine()

    def generate(
        self,
        workbook:Workbook,
        profile: WorkbookProfile,
    ) -> DashboardData:
        """
        Generate the dashboard.
        """

        dashboard = self.recommender.recommend(profile)

        plan = self.planner.plan(dashboard)

        return self.engine.build(workbook,plan)
