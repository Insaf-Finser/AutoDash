from pathlib import Path

from app.services.dashboard.generator import DashboardGenerator
from app.services.profiling.profiler import Profiler

excel_file = Path("storage/workbooks/bc64ffb2-6555-4621-a019-3edaf12fc96a.xlsx")


data = excel_file.read_bytes()

profile = Profiler().profile(data)

dashboard = DashboardGenerator().generate(profile)

print(dashboard.model_dump_json(indent=2))