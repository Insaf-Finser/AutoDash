from pathlib import Path

from app.services.dashboard.generator import DashboardGenerator
from app.services.profiler.profiler import Profiler
from app.services.profiler.loader import WorkbookLoader

excel_file = Path("storage/workbooks/bc64ffb2-6555-4621-a019-3edaf12fc96a.xlsx")


data = excel_file.read_bytes()

workbook = WorkbookLoader().load(data)
profile = Profiler().profile(workbook)

dashboard = DashboardGenerator().generate(workbook,profile)

print(dashboard.model_dump_json(indent=2))