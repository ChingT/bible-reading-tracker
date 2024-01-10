from datetime import datetime
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel
from .plan import Plan
from .unit import ScheduleUnitLink, Unit


class DailySchedule(BaseUUIDModel, table=True):
    __tablename__ = "daily_schedule"

    plan: Plan = Relationship(back_populates="daily_schedules")
    plan_id: UUID = Field(foreign_key="plan.id")
    date: datetime = Field(unique=True)
    units: list[Unit] = Relationship(
        back_populates="daily_schedules",
        link_model=ScheduleUnitLink,
        sa_relationship_kwargs={"lazy": "subquery"},
    )


class DailyScheduleBase(SQLModel):
    plan_id: UUID
    date: datetime
    units: list[Unit] = []


class DailyScheduleCreate(DailyScheduleBase):
    pass


class DailyScheduleUpdate(SQLModel):
    plan_id: UUID | None = None
    date: datetime | None = None
    units: list[Unit] = []


class DailyScheduleOut(BaseUUIDModel, DailyScheduleBase):
    units: list[Unit]
