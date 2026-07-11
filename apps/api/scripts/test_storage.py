import asyncio

from app.services.storage import get_storage_service


async def main():
    storage = get_storage_service()

    object_key = await storage.save(
        "hello.txt",
        b"InsightForge Storage Test",
    )

    print("Saved:", object_key)

    print("Exists:", await storage.exists(object_key))

    content = await storage.read(object_key)

    print(content.decode())

    await storage.delete(object_key)

    print("Deleted")


asyncio.run(main())