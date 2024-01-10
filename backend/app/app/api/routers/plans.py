from uuid import UUID

from fastapi import APIRouter, Query

from app import crud
from app.api.deps import SessionDep
from app.models.plan import PlanOut
from app.models.schedule import ScheduleOut

router = APIRouter()


@router.get("/")
async def list_plans(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> list[PlanOut]:
    """Retrieve bible reading plans."""
    return await crud.plan.list(session, offset, limit)


@router.get("/{plan_id}/schedules")
async def list_schedules(
    session: SessionDep,
    plan_id: UUID,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[ScheduleOut]:
    """Retrieve daily schedules."""
    return await crud.schedule.list_from_plan(session, plan_id, offset, limit)
