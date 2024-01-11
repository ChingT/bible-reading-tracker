from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel
from .plan import Plan
from .unit import ScheduleUnitLink, Unit

if TYPE_CHECKING:
    from .user_schedule_link import UserScheduleLink


class Schedule(BaseUUIDModel, table=True):
    __tablename__ = "schedule"

    plan: Plan = Relationship(back_populates="schedules")
    plan_id: UUID = Field(foreign_key="plan.id")
    date: datetime = Field(unique=True)
    units: list[Unit] = Relationship(
        back_populates="schedules",
        link_model=ScheduleUnitLink,
        sa_relationship_kwargs={"lazy": "subquery"},
    )
    user_links: list["UserScheduleLink"] = Relationship(
        back_populates="finished_schedule"
    )


class ScheduleBase(SQLModel):
    plan_id: UUID
    date: datetime
    units: list[Unit] = []


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(SQLModel):
    plan_id: UUID | None = None
    date: datetime | None = None
    units: list[Unit] = []


class ScheduleOut(BaseUUIDModel, ScheduleBase):
    units: list[Unit]
