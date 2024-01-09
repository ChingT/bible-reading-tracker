from fastapi import APIRouter, Query

from app import crud
from app.api.deps import SessionDep
from app.models.book import BookOut
from app.models.unit import UnitOut

router = APIRouter()


@router.get("/")
async def list_books(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> list[BookOut]:
    """Retrieve books."""
    return await crud.book.list(session, offset, limit)


@router.get("/units")
async def list_units(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> list[UnitOut]:
    """Retrieve units."""
    return await crud.unit.list(session, offset, limit)
