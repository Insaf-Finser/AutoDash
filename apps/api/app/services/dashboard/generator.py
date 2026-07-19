from app.services.dashboard.models import Dashboard
from app.services.dashboard.recommender import DashboardRecommender
from app.services.profiler.models import WorkbookProfile


class DashboardGenerator:
    """
    Generates a dashboard from a workbook profile.
    """

    def __init__(self):
        self.recommender = DashboardRecommender()

    def generate(
        self,
        profile: WorkbookProfile,
    ) -> Dashboard:
        """
        Generate the dashboard.
        """

        dashboard = self.recommender.recommend(profile)

        return dashboard