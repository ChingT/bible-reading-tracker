import csv
from pathlib import Path

from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.core.config import settings
from app.main import logger
from app.models.book import BookCreate, BookEnum
from app.models.plan import PlanCreate
from app.models.user import UserCreateFromUser

source_root = Path("app/initial_data")


async def create_superuser(session: AsyncSession) -> None:
    if user := await crud.user.get_by_email(session, settings.FIRST_SUPERUSER_EMAIL):
        logger.info("Superuser %s exists in database", user)
        return

    new_user = UserCreateFromUser(
        email=settings.FIRST_SUPERUSER_EMAIL,
        password=settings.FIRST_SUPERUSER_PASSWORD,
        display_name="admin",
    )
    user = await crud.user.create_from_user(session, new_user, is_superuser=True)
    await crud.user.activate(session, user)
    logger.info("Superuser created: %s", user)


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
                logger.info("Plan created: %s", plan)


async def populate_books(session: AsyncSession) -> None:
    csv_file_path = source_root / "bible_books.csv"
    with Path.open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for index, row in enumerate(csv_reader):
            if await crud.book.get_by_attr(session, short_name_de=row["short_name_de"]):
                continue

            data = dict(**row)
            data["book_type"] = BookEnum(row["book_type"])
            data["order"] = index + 1
            data_in = BookCreate.model_validate(data)
            book = await crud.book.create(session, data_in)
            logger.info("Book created: %s", book)
