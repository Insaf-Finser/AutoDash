from pathlib import Path

from app.services.profiling.profiler import Profiler

profiler = Profiler()

data = Path("storage/workbooks/bc64ffb2-6555-4621-a019-3edaf12fc96a.xlsx").read_bytes()

profile = profiler.profile(data)

print(profile.model_dump_json(indent=2))