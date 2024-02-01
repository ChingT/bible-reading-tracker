from typing import Any

from fastapi import APIRouter, Query

from app import crud
from app.api.deps import SessionDep
from app.models.book import BookEnum, BookOut
from app.models.passage import PassageOut

router = APIRouter()


@router.get("/{book_type}", response_model=list[BookOut])
async def list_books(
    session: SessionDep,
    book_type: BookEnum | None = None,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> Any:
    """Retrieve books."""
    return await crud.book.list_by_book_type(session, book_type, offset, limit)


@router.get("/passages", response_model=list[PassageOut])
async def list_passages(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> Any:
    """Retrieve passages."""
    return await crud.passage.list(session, offset, limit)
