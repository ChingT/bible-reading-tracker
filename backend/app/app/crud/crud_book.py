from collections.abc import Sequence
from uuid import UUID

from sqlmodel import SQLModel, or_, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.book import Book, BookCreate, BookEnum
from app.models.unit import Unit, UnitCreate


class CRUDBook(CRUDBase[Book, BookCreate, SQLModel]):
    async def get_by_name(self, session: AsyncSession, full_name: str) -> Book | None:
        query = select(Book).where(Book.full_name == full_name)
        result = await session.exec(query)
        return result.first()

    async def list_by_book_type(
        self,
        session: AsyncSession,
        book_type: BookEnum | None = None,
        offset: int = 0,
        limit: int = 100,
    ) -> Sequence[Book]:
        query = (
            select(Book)
            .where(or_(book_type is None, Book.book_type == book_type))
            .order_by(Book.order)
            .offset(offset)
            .limit(limit)
        )
        result = await session.exec(query)
        return result.all()


class CRUDUnit(CRUDBase[Unit, UnitCreate, SQLModel]):
    async def list_by_book_type(
        self,
        session: AsyncSession,
        book_type: BookEnum | None = None,
        offset: int = 0,
        limit: int | None = 100,
    ) -> Sequence[Unit]:
        query = (
            select(Unit)
            .where(or_(book_type is None, Book.book_type == book_type))
            .join(Book)
            .order_by(Book.order)
            .order_by(Unit.chapter)
            .offset(offset)
            .limit(limit)
        )
        result = await session.exec(query)
        return result.all()

    async def get_by_book_chapter(
        self, session: AsyncSession, book_id: UUID, chapter: int
    ) -> Unit | None:
        query = select(Unit).where(Unit.book_id == book_id, Unit.chapter == chapter)
        result = await session.exec(query)
        return result.first()


book = CRUDBook(Book)
unit = CRUDUnit(Unit)
