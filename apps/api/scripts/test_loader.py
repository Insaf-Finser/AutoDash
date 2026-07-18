from pathlib import Path

from app.services.profiling.loader import WorkbookLoader

loader = WorkbookLoader()

data = Path("storage/workbooks/52a926e6-08ab-4128-9865-5fdca1949b6e.xlsx").read_bytes()

workbook = loader.load(data)

print(workbook.keys())