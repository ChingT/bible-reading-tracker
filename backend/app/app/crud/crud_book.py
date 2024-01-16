from collections.abc import Sequence
from uuid import UUID

from sqlmodel import SQLModel, or_, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.book import Book, BookCreate, BookEnum
from app.models.passage import Passage, PassageCreate


class CRUDBook(CRUDBase[Book, BookCreate, SQLModel]):
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


class CRUDPassage(CRUDBase[Passage, PassageCreate, SQLModel]):
    async def list_by_book_type(
        self,
        session: AsyncSession,
        book_type: BookEnum | None = None,
        offset: int = 0,
        limit: int | None = 100,
    ) -> Sequence[Passage]:
        query = (
            select(Passage)
            .where(or_(book_type is None, Book.book_type == book_type))
            .join(Book)
            .order_by(Book.order)
            .order_by(Passage.verses)
            .offset(offset)
            .limit(limit)
        )
        result = await session.exec(query)
        return result.all()

    async def get_by_book_verses(
        self, session: AsyncSession, book_id: UUID, verses: str
    ) -> Passage | None:
        query = select(Passage).where(
            Passage.book_id == book_id, Passage.verses == verses
        )
        result = await session.exec(query)
        return result.first()


book = CRUDBook(Book)
passage = CRUDPassage(Passage)
