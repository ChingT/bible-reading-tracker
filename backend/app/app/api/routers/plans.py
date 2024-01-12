from typing import Any

from fastapi import APIRouter, Query

from app import crud
from app.api.deps import CurrentUser, SessionDep
from app.api.utils import PlanDep, ScheduleDep
from app.models.plan import PlanOut
from app.models.schedule import ScheduleOut

router = APIRouter()


@router.get("/", response_model=list[PlanOut])
async def list_plans(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> Any:
    """Retrieve bible reading plans."""
    return await crud.plan.list(session, offset, limit)


@router.get("/{plan_id}/schedules_without_logged_in")
async def list_schedules_without_logged_in(
    session: SessionDep,
    plan: PlanDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[ScheduleOut]:
    """Retrieve daily schedules without user needed to be logged-in."""
    schedules = await crud.schedule.list_from_plan(session, plan.id, offset, limit)
    return [ScheduleOut.construct(schedule) for schedule in schedules]


@router.get("/{plan_id}/schedules")
async def list_schedules(
    session: SessionDep,
    current_user: CurrentUser,
    plan: PlanDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[ScheduleOut]:
    """Retrieve daily schedules.

    For each a schedule, show if it is finished by the logged-in user.
    """
    schedules = await crud.schedule.list_from_plan(session, plan.id, offset, limit)
    return [ScheduleOut.construct(schedule, current_user) for schedule in schedules]


@router.get("/finished_schedule")
async def list_schedules_finished_by_user(
    session: SessionDep,
    current_user: CurrentUser,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[ScheduleOut]:
    """Retrieve finished daily schedules for the logged-in user."""
    schedules = await crud.schedule.list_finished_by_user(
        session, current_user.id, offset, limit
    )
    return [ScheduleOut.construct(schedule, current_user) for schedule in schedules]


@router.patch("/finished_schedule/{schedule_id}")
async def toggle_finished_schedule(
    session: SessionDep, current_user: CurrentUser, schedule: ScheduleDep
) -> ScheduleOut:
    """Toggle finished daily schedule for the logged-in user."""
    schedule = await crud.schedule.toggle_finished(session, schedule, current_user)
    return ScheduleOut.construct(schedule, current_user)
