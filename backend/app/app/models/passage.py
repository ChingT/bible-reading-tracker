from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from .base_model import BaseUUIDModel
from .book import Book

if TYPE_CHECKING:
    from .schedule import Schedule


class SchedulePassageLink(SQLModel, table=True):
    __tablename__ = "schedule_passage_link"

    schedule_id: UUID = Field(foreign_key="schedule.id", primary_key=True)
    passage_id: UUID = Field(foreign_key="passage.id", primary_key=True)


class Passage(BaseUUIDModel, table=True):
    __table_args__ = (UniqueConstraint("book_id", "verses"),)
    book: Book = Relationship(back_populates="passages")
    book_id: UUID = Field(foreign_key="book.id")
    verses: str
    schedules: list["Schedule"] = Relationship(
        back_populates="passages", link_model=SchedulePassageLink
    )


class PassageBase(SQLModel):
    book_id: UUID
    verses: str


class PassageCreate(PassageBase):
    pass


class PassageOut(BaseUUIDModel, PassageBase):
    pass
