import asyncio

from app.db.session import SessionLocal
from app.utils.populate_database import create_superuser, populate_books_units


async def main() -> None:
    async with SessionLocal() as session:
        await create_superuser(session)
        await populate_books_units(session)


if __name__ == "__main__":
    asyncio.run(main())
