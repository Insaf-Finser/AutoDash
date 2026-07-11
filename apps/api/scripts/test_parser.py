from pathlib import Path

from app.services.parser import WorkbookParser

parser = WorkbookParser()

data = Path("storage/workbooks/<your_file>.xlsx").read_bytes()

metadata = parser.extract_metadata(data)

print(metadata)