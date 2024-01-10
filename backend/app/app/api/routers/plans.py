from uuid import UUID

from fastapi import APIRouter, Query

from app import crud
from app.api.deps import SessionDep
from app.models.daily_schedule import DailyScheduleOut
from app.models.plan import PlanOut

router = APIRouter()


@router.get("/")
async def list_plans(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> list[PlanOut]:
    """Retrieve bible reading plans."""
    return await crud.plan.list(session, offset, limit)


@router.get("/{plan_id}/daily_schedules")
async def list_daily_schedules(
    session: SessionDep,
    plan_id: UUID,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[DailyScheduleOut]:
    """Retrieve daily schedules."""
    return await crud.daily_schedule.list_from_plan(session, plan_id, offset, limit)
