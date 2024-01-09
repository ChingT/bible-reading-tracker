from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.plan import Plan, PlanCreate, PlanOut


class CRUDPlan(CRUDBase[Plan, PlanCreate, SQLModel]):
    async def get_by_title(self, session: AsyncSession, title: str) -> PlanOut | None:
        query = select(self.model).where(self.model.title == title)
        result = await session.exec(query)
        return result.first()


plan = CRUDPlan(Plan)
