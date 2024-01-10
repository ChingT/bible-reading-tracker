import csv
from pathlib import Path

from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.core.config import settings
from app.main import logger
from app.models.book import BookCreate, BookEnum
from app.models.plan import PlanCreate
from app.models.unit import UnitCreate
from app.models.user import UserCreate

source_root = Path("app/initial_data")


async def create_superuser(session: AsyncSession) -> None:
    if user := await crud.user.get_by_email(session, settings.FIRST_SUPERUSER_EMAIL):
        logger.info("Superuser %s exists in database", user)
        return

    new_user = UserCreate(
        email=settings.FIRST_SUPERUSER_EMAIL,
        password=settings.FIRST_SUPERUSER_PASSWORD,
        display_name="admin",
    )
    user = await crud.user.create(session, new_user, is_superuser=True)
    await crud.user.activate(session, user)
    logger.info("Superuser %s created", user)


async def populate_books_units(session: AsyncSession) -> None:
    csv_file_path = source_root / "bible_books.csv"
    with Path.open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for index, data in enumerate(csv_reader):
            if not (book := await crud.book.get_by_name(session, data["full_name"])):
                data_in = BookCreate(
                    full_name=data["full_name"],
                    short_name=data["short_name"],
                    book_type=BookEnum(data["book_type"]),
                    order=index + 1,
                )
                book = await crud.book.create(session, data_in)
                logger.info("Book %s created", book)

            for chapter in range(1, int(data["num_chapters"]) + 1):
                if not (
                    await crud.unit.get_by_book_chapter(
                        session, book_id=book.id, chapter=chapter
                    )
                ):
                    unit = await crud.unit.create(
                        session, UnitCreate(book_id=book.id, chapter=chapter)
                    )
                    logger.info("Unit %s created", unit)


async def populate_plans(session: AsyncSession) -> None:
    csv_file_path = source_root / "reading_plans.csv"
    with Path.open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data = dict(**row)

            if not (await crud.plan.get_by_title(session, data["title"])):
                data_in = PlanCreate(
                    title=data["title"], description=data["description"]
                )
                plan = await crud.plan.create(session, data_in)
                logger.info("Plan %s created", plan)
