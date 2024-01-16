from typing import Any

from fastapi import APIRouter, Query

from app import crud
from app.api.deps import SessionDep
from app.models.book import BookOut
from app.models.passage import PassageOut

router = APIRouter()


@router.get("/", response_model=list[BookOut])
async def list_books(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> Any:
    """Retrieve books."""
    return await crud.book.list(session, offset, limit)


@router.get("/passages", response_model=list[PassageOut])
async def list_passages(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> Any:
    """Retrieve passages."""
    return await crud.passage.list(session, offset, limit)
