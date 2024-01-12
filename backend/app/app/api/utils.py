from typing import Annotated, TypeVar
from uuid import UUID

from fastapi import Depends
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from app.api.deps import SessionDep
from app.api.exceptions import IdNotFoundException
from app.models.plan import Plan
from app.models.schedule import Schedule

ModelType = TypeVar("ModelType", bound=SQLModel)


def get_or_404(session: AsyncSession, model: type[ModelType], model_id: UUID):
    """Fetch a model instance by its ID or raise a 404 error if not found.

    session (Session): Database session to execute the operation.
    model (ModelType): The model class to fetch.
    model_id (UUID): The ID of the model instance to fetch.

    Returns
    -------
    models.Base: The fetched model instance.
    """
    if instance := session.get(model, model_id):
        return instance
    raise IdNotFoundException(model, model_id)


async def get_schedule_or_404(schedule_id: UUID, session: SessionDep) -> Schedule:
    if schedule := await session.get(Schedule, schedule_id):
        return schedule
    raise IdNotFoundException(Schedule, schedule_id)


async def get_plan_or_404(plan_id: UUID, session: SessionDep) -> Plan:
    if plan := await session.get(Plan, plan_id):
        return plan
    raise IdNotFoundException(Plan, plan_id)


ScheduleDep = Annotated[Schedule, Depends(get_schedule_or_404)]
PlanDep = Annotated[Plan, Depends(get_plan_or_404)]
