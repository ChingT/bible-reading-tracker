from uuid import UUID

from sqlmodel import SQLModel, or_, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.book import Book, BookCreate, BookEnum, BookOut
from app.models.unit import Unit, UnitCreate


class CRUDBook(CRUDBase[Book, BookCreate, SQLModel]):
    async def get_by_name(
        self, session: AsyncSession, full_name: str
    ) -> BookOut | None:
        query = select(self.model).where(self.model.full_name == full_name)
        result = await session.exec(query)
        return result.first()

    async def list(
        self,
        session: AsyncSession,
        book_type: BookEnum | None = None,
        offset: int = 0,
        limit: int = 100,
    ) -> BookOut | None:
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
    ) -> BookOut | None:
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
    ) -> BookOut | None:
        query = select(self.model).where(
            self.model.book_id == book_id, self.model.chapter == chapter
        )
        result = await session.exec(query)
        return result.first()


book = CRUDBook(Book)
unit = CRUDUnit(Unit)
