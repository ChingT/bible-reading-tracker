from collections.abc import Sequence
from uuid import UUID

from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.daily_schedule import DailySchedule, DailyScheduleCreate
from app.models.plan import Plan, PlanCreate, PlanOut


class CRUDPlan(CRUDBase[Plan, PlanCreate, SQLModel]):
    async def get_by_title(self, session: AsyncSession, title: str) -> PlanOut | None:
        query = select(Plan).where(Plan.title == title)
        result = await session.exec(query)
        return result.first()


class CRUDDailySchedule(CRUDBase[DailySchedule, DailyScheduleCreate, SQLModel]):
    async def list_from_plan(
        self, session: AsyncSession, plan_id: UUID, offset: int = 0, limit: int = 100
    ) -> Sequence[DailySchedule]:
        query = (
            select(DailySchedule)
            .where(DailySchedule.plan_id == plan_id)
            .order_by(DailySchedule.date)
            .offset(offset)
            .limit(limit)
        )
        result = await session.exec(query)
        return result.all()


plan = CRUDPlan(Plan)
daily_schedule = CRUDDailySchedule(DailySchedule)
