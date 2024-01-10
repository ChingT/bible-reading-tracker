from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel
from .book import Book

if TYPE_CHECKING:
    from .daily_schedule import DailySchedule


class ScheduleUnitLink(SQLModel, table=True):
    __tablename__ = "schedule_unit_link"

    daily_schedule_id: UUID = Field(foreign_key="daily_schedule.id", primary_key=True)
    unit_id: UUID = Field(foreign_key="unit.id", primary_key=True)


class Unit(BaseUUIDModel, table=True):
    book: Book = Relationship(back_populates="units")
    book_id: UUID = Field(foreign_key="book.id")
    chapter: int
    daily_schedules: list["DailySchedule"] = Relationship(
        back_populates="units", link_model=ScheduleUnitLink
    )


class UnitBase(SQLModel):
    book_id: UUID
    chapter: int


class UnitCreate(UnitBase):
    pass


class UnitOut(BaseUUIDModel, UnitBase):
    pass
