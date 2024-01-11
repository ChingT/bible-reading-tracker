from collections.abc import Sequence
from uuid import UUID

from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.plan import Plan, PlanCreate
from app.models.schedule import Schedule, ScheduleCreate
from app.models.user_schedule_link import UserScheduleLink, UserScheduleLinkCreate


class CRUDPlan(CRUDBase[Plan, PlanCreate, SQLModel]):
    async def get_by_title(self, session: AsyncSession, title: str) -> Plan | None:
        query = select(Plan).where(Plan.title == title)
        result = await session.exec(query)
        return result.first()


class CRUDSchedule(CRUDBase[Schedule, ScheduleCreate, SQLModel]):
    async def list_from_plan(
        self, session: AsyncSession, plan_id: UUID, offset: int = 0, limit: int = 100
    ) -> Sequence[Schedule]:
        query = (
            select(Schedule)
            .where(Schedule.plan_id == plan_id)
            .order_by(Schedule.date)
            .offset(offset)
            .limit(limit)
        )
        result = await session.exec(query)
        return result.all()


class CRUDUserSchedule(CRUDBase[UserScheduleLink, UserScheduleLinkCreate, SQLModel]):
    async def list_by_plan_and_user(
        self, session: AsyncSession, user_id: UUID, plan_id: UUID
    ) -> Sequence[UserScheduleLink]:
        query = (
            select(UserScheduleLink)
            .join(Schedule)
            .where(Schedule.plan_id == plan_id)
            .where(UserScheduleLink.user_id == user_id)
            .order_by(UserScheduleLink.created_at)
        )
        result = await session.exec(query)
        return result.all()


plan = CRUDPlan(Plan)
schedule = CRUDSchedule(Schedule)
user_schedule_link = CRUDUserSchedule(UserScheduleLink)
