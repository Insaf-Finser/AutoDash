import asyncio
from uuid import uuid4

from app.database.session import AsyncSessionLocal
from app.repositories.workbook_repository import WorkbookRepository


async def main():
    async with AsyncSessionLocal() as session:

        repo = WorkbookRepository(session)

        workbook = await repo.create(
            name="Repository Test",
            original_filename="test.xlsx",
            stored_filename=f"{uuid4()}.xlsx",
            storage_key=f"workbooks/{uuid4()}.xlsx",
            mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            file_extension=".xlsx",
            file_size=1024,
        )

        print("Created")
        print(workbook.id)

        found = await repo.get_by_id(workbook.id)

        print("Retrieved")
        print(found.name)

        await repo.delete(found)

        deleted = await repo.get_by_id(workbook.id)

        print("Deleted:", deleted)


if __name__ == "__main__":
    asyncio.run(main())