from uuid import UUID

from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.book import Book, BookCreate, BookOut
from app.models.unit import Unit, UnitCreate


class CRUDBook(CRUDBase[Book, BookCreate, SQLModel]):
    async def get_by_name(
        self, session: AsyncSession, full_name: str
    ) -> BookOut | None:
        query = select(self.model).where(self.model.full_name == full_name)
        result = await session.exec(query)
        return result.first()


class CRUDUnit(CRUDBase[Unit, UnitCreate, SQLModel]):
    async def get_by_book_chapter(
        self, session: AsyncSession, book_id: UUID, chapter: int
    ) -> BookOut | None:
        query = select(self.model).where(
            self.model.book_id == book_id and self.model.chapter == chapter
        )
        result = await session.exec(query)
        return result.first()


book = CRUDBook(Book)
unit = CRUDUnit(Unit)
