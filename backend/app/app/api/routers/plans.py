from typing import Annotated, Any

from fastapi import APIRouter, Query

from app import crud
from app.api.deps import CurrentUser, PlanDep, ScheduleDep, SessionDep, UserDep
from app.models.plan import PlanOut
from app.models.schedule import ScheduleOut

router = APIRouter()

OFFSET_QUERY = Annotated[int, Query(ge=0)]
LIMIT_QUERY = Annotated[int, Query(le=366)]


@router.get("", response_model=list[PlanOut])
async def list_plans(
    session: SessionDep, offset: OFFSET_QUERY = 0, limit: LIMIT_QUERY = 100
) -> Any:
    """Retrieve bible reading plans."""
    return await crud.plan.list(session, offset, limit)


@router.get("/{plan_id}/schedules_without_logged_in")
async def list_schedules_without_logged_in(
    session: SessionDep,
    plan: PlanDep,
    offset: OFFSET_QUERY = 0,
    limit: LIMIT_QUERY = 366,
) -> list[ScheduleOut]:
    """Retrieve daily schedules without user needed to be logged-in."""
    schedules = await crud.schedule.list_from_plan(session, plan.id, offset, limit)
    return [ScheduleOut.construct(schedule) for schedule in schedules]


@router.get("/{plan_id}/schedules")
async def list_schedules(
    session: SessionDep,
    current_user: CurrentUser,
    plan: PlanDep,
    offset: OFFSET_QUERY = 0,
    limit: LIMIT_QUERY = 366,
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
    offset: OFFSET_QUERY = 0,
    limit: LIMIT_QUERY = 366,
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


@router.get("/{plan_id}/progress/{user_id}")
async def get_progress(session: SessionDep, plan: PlanDep, user: UserDep) -> int:
    """Retrieve the number of finished schedules of a plan for the user."""
    return await crud.schedule.get_num_finished_schedules(session, plan.id, user.id)
