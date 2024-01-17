import csv
import datetime
from pathlib import Path

from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.api.exceptions import NameNotFoundException
from app.main import logger
from app.models.book import Book
from app.models.passage import PassageCreate
from app.models.plan import Plan
from app.models.schedule import ScheduleCreate

YEAR = 2024

source_root = Path("app/initial_data")


async def populate_schedules(session: AsyncSession) -> None:
    name = "Sechsmonatiger Lesezeitplan"
    plan = await crud.plan.get_by_title(session, name)
    if plan is None:
        raise NameNotFoundException(Plan, name)

    all_dates = get_dates_of_year(YEAR)

    csv_file_path = source_root / "daily_passage.csv"
    with Path.open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row, day in zip(csv_reader, all_dates, strict=False):
            if schedule := await crud.schedule.get_by_attr(session, date=day):
                logger.info("Schedule exists: %s", schedule)
                continue

            passages = [
                await get_passage_from_str(session, passage_str)
                for passage_str in row["verses"].split(";")
            ]
            schedule = await crud.schedule.create(
                session, ScheduleCreate(plan_id=plan.id, date=day, passages=passages)
            )
            logger.info("schedule created %s", schedule)


async def get_passage_from_str(session: AsyncSession, passage_str: str):
    *short_name, verses = passage_str.split(" ")
    short_name_en = " ".join(short_name)
    book = await crud.book.get_by_attr(session, short_name_en=short_name_en)
    if book is None:
        raise NameNotFoundException(Book, short_name_en)
    if passage := await crud.passage.get_by_attr(
        session, book_id=book.id, verses=verses
    ):
        logger.info("Passage exists: %s", passage)
    else:
        data_in = PassageCreate(book_id=book.id, verses=verses)
        passage = await crud.passage.create(session, data_in)
        logger.info("Passage created: %s", passage)
    return passage


def get_dates_of_year(year: int) -> list[datetime.date]:
    """Return a list of all dates of a given year."""
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year + 1, 1, 1)
    num_days = (end_date - start_date).days
    return [(start_date + datetime.timedelta(days=days)) for days in range(num_days)]
