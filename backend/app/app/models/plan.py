from typing import TYPE_CHECKING

from sqlmodel import Relationship, SQLModel

from .base_model import BaseUUIDModel

if TYPE_CHECKING:
    from .daily_schedule import DailySchedule


class Plan(BaseUUIDModel, table=True):
    title: str
    description: str

    daily_schedules: list["DailySchedule"] = Relationship(back_populates="plan")


class PlanBase(SQLModel):
    title: str
    description: str


class PlanCreate(PlanBase):
    pass


class PlanUpdate(SQLModel):
    title: str | None = None
    description: str | None = None


class PlanOut(BaseUUIDModel, PlanBase):
    pass
