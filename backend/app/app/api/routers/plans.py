from typing import Any
from uuid import UUID

from fastapi import APIRouter, Query, status
from fastapi.responses import Response

from app import crud
from app.api.deps import CurrentUser, SessionDep
from app.api.exceptions import IdNotFoundException
from app.models.plan import PlanOut
from app.models.schedule import Schedule, ScheduleOut
from app.models.user import User
from app.models.user_schedule_link import (
    UserScheduleLink,
    UserScheduleLinkCreate,
    UserScheduleLinkOut,
)

router = APIRouter()


@router.get("/", response_model=list[PlanOut])
async def list_plans(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> Any:
    """Retrieve bible reading plans."""
    return await crud.plan.list(session, offset, limit)


@router.get("/{plan_id}/schedules", response_model=list[ScheduleOut])
async def list_schedules(
    session: SessionDep,
    plan_id: UUID,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> Any:
    """Retrieve daily schedules."""
    return await crud.schedule.list_from_plan(session, plan_id, offset, limit)


@router.get("/{plan_id}/user_schedule_links", response_model=list[UserScheduleLinkOut])
async def list_user_schedule_links(
    session: SessionDep, current_user: CurrentUser, plan_id: UUID
) -> Any:
    """Retrieve finished daily schedules from the plan for the logged-in user."""
    return await crud.user_schedule_link.list_by_plan_and_user(
        session, current_user.id, plan_id
    )


@router.patch("/finished_schedule/{schedule_id}", response_model=UserScheduleLinkOut)
async def toggle_finished_schedule(
    session: SessionDep, current_user: CurrentUser, schedule_id: UUID
) -> Any:
    """Toggle finished daily schedule for the logged-in user."""
    if user_schedule_link := await get_user_schedule_link(
        session, user_id=current_user.id, finished_schedule_id=schedule_id
    ):
        await crud.user_schedule_link.delete(session, user_schedule_link)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    obj_in = UserScheduleLinkCreate(
        user_id=current_user.id, finished_schedule_id=schedule_id
    )
    return await crud.user_schedule_link.create(session, obj_in)


async def varify_user_schedule_link(
    session: SessionDep, user_id: UUID, finished_schedule_id: UUID
) -> None:
    if not (await crud.user.get(session, id=user_id)):
        raise IdNotFoundException(User, user_id)

    if not (await crud.schedule.get(session, id=finished_schedule_id)):
        raise IdNotFoundException(Schedule, finished_schedule_id)


async def get_user_schedule_link(
    session: SessionDep, user_id: UUID, finished_schedule_id: UUID
) -> UserScheduleLink | None:
    await varify_user_schedule_link(session, user_id, finished_schedule_id)

    return await crud.user_schedule_link.get(
        session, user_id=user_id, finished_schedule_id=finished_schedule_id
    )
