from collections.abc import Sequence
from uuid import UUID

from sqlmodel import SQLModel, func, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.plan import Plan, PlanCreate
from app.models.schedule import Schedule, ScheduleCreate
from app.models.user import User, UserScheduleLink


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

    async def toggle_finished(
        self, session: AsyncSession, schedule: Schedule, user: User
    ) -> Schedule:
        if user in schedule.finished_users:
            schedule.finished_users.remove(user)
        else:
            schedule.finished_users.append(user)
        session.add(schedule)
        await session.commit()
        return schedule

    async def list_finished_by_user(
        self, session: AsyncSession, user_id: UUID, offset: int = 0, limit: int = 100
    ) -> Sequence[Schedule]:
        query = (
            select(Schedule)
            .join(UserScheduleLink)
            .where(UserScheduleLink.user_id == user_id)
            .order_by(Schedule.date)
            .offset(offset)
            .limit(limit)
        )
        result = await session.exec(query)
        return result.all()

    async def get_num_finished_schedules(
        self, session: AsyncSession, plan_id: UUID, user_id: UUID
    ) -> int:
        query = (
            select(func.count(Schedule.id))
            .join(UserScheduleLink)
            .where(Schedule.plan_id == plan_id, UserScheduleLink.user_id == user_id)
        )
        result = await session.exec(query)
        return result.one()


plan = CRUDPlan(Plan)
schedule = CRUDSchedule(Schedule)
