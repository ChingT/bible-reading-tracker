from datetime import date, timedelta

from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.main import logger
from app.models.book import BookEnum
from app.models.schedule import ScheduleCreate

YEAR = 2024
NUM_OF_UNITS_PER_DAY = 2


async def populate_schedules(session: AsyncSession) -> None:
    plan = await crud.plan.get_by_title(session, "Sechsmonatiger Lesezeitplan")
    units = await crud.unit.list_by_book_type(
        session, book_type=BookEnum.NT, limit=None
    )
    all_dates = get_dates_of_year(YEAR)
    index = 0
    for day in all_dates:
        if is_weekday(day):
            daily_units = units[index : index + NUM_OF_UNITS_PER_DAY]
            index += NUM_OF_UNITS_PER_DAY
        else:
            daily_units = []

        schedule = await crud.schedule.create(
            session, ScheduleCreate(plan_id=plan.id, date=day, units=daily_units)
        )
        logger.info("schedule %s created.", schedule)


def get_dates_of_year(year: int) -> list[date]:
    """Return a list of all dates of a given year."""
    start_date = date(year, 1, 1)
    end_date = date(year + 1, 1, 1)
    num_days = (end_date - start_date).days
    return [(start_date + timedelta(days=days)) for days in range(num_days)]


def is_weekday(day: date) -> bool:
    """Return True if day is a weekday."""
    return day.isoweekday() in range(1, 6)


if __name__ == "__main__":
    get_dates_of_year(2024)
