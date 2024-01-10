from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel

if TYPE_CHECKING:
    from app.models.unit import Unit


class BookEnum(str, Enum):
    NT = "New Testament"
    OT = "Old Testament"


class Book(BaseUUIDModel, table=True):
    full_name: str = Field(unique=True)
    short_name: str = Field(unique=True)
    book_type: BookEnum
    order: int

    units: list["Unit"] = Relationship(back_populates="book")


class BookBase(SQLModel):
    full_name: str
    short_name: str
    book_type: BookEnum
    order: int


class BookCreate(BookBase):
    pass


class BookOut(BaseUUIDModel, BookBase):
    pass
