from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel

if TYPE_CHECKING:
    from app.models.passage import Passage


class BookEnum(str, Enum):
    NT = "New Testament"
    OT = "Old Testament"


class Book(BaseUUIDModel, table=True):
    full_name_de: str = Field(unique=True)
    short_name_de: str = Field(unique=True)
    full_name_en: str = Field(unique=True)
    short_name_en: str = Field(unique=True)
    book_type: BookEnum
    order: int

    passages: list["Passage"] = Relationship(back_populates="book")


class BookBase(SQLModel):
    full_name_de: str
    short_name_de: str
    full_name_en: str
    short_name_en: str
    book_type: BookEnum
    order: int


class BookCreate(BookBase):
    pass


class BookOut(BaseUUIDModel, BookBase):
    pass
