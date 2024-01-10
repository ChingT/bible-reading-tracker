from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .daily_schedule import DailySchedule

if TYPE_CHECKING:
    from .user import User


class UserScheduleLink(SQLModel, table=True):
    __tablename__ = "user_schedule_link"

    user_id: UUID = Field(foreign_key="user.id", primary_key=True)
    finished_schedule_id: UUID = Field(
        foreign_key="daily_schedule.id", primary_key=True
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="finished_schedule_links")
    finished_schedule: DailySchedule = Relationship(back_populates="user_links")


class UserScheduleLinkBase(SQLModel):
    user_id: UUID
    finished_schedule_id: UUID


class UserScheduleLinkCreate(UserScheduleLinkBase):
    pass


class UserScheduleLinkOut(UserScheduleLinkBase):
    created_at: datetime
