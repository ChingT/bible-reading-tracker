from fastapi import APIRouter, Query

from app import crud
from app.api.deps import SessionDep
from app.models.plan import PlanOut

router = APIRouter()


@router.get("/")
async def list_plans(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> list[PlanOut]:
    """Retrieve bible reading plans."""
    return await crud.plan.list(session, offset, limit)
