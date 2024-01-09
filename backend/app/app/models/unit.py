from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel
from .book import Book


class Unit(BaseUUIDModel, table=True):
    book: Book = Relationship(back_populates="units")
    book_id: UUID = Field(foreign_key="book.id")
    chapter: int


class UnitBase(SQLModel):
    book_id: UUID
    chapter: int


class UnitCreate(UnitBase):
    pass


class UnitOut(BaseUUIDModel, UnitBase):
    pass
