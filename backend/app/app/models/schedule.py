import datetime
from uuid import UUID

from pydantic import FieldValidationInfo, field_validator
from sqlmodel import Field, Relationship, SQLModel

from .base_model import BaseUUIDModel
from .passage import Passage, SchedulePassageLink
from .plan import Plan
from .user import User, UserScheduleLink


class Schedule(BaseUUIDModel, table=True):
    __tablename__ = "schedule"

    plan: Plan = Relationship(back_populates="schedules")
    plan_id: UUID = Field(foreign_key="plan.id")
    date: datetime.date = Field(unique=True)
    passages: list[Passage] = Relationship(
        back_populates="schedules",
        link_model=SchedulePassageLink,
        sa_relationship_kwargs={"lazy": "subquery"},
    )
    finished_users: list[User] = Relationship(
        back_populates="finished_schedules",
        link_model=UserScheduleLink,
        sa_relationship_kwargs={"lazy": "subquery"},
    )


class ScheduleBase(SQLModel):
    plan_id: UUID
    date: datetime.date
    passages: list[Passage] = []


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleOut(BaseUUIDModel, ScheduleBase):
    passages: list[Passage]
    is_finished_by_logged_in_user: bool = False

    @classmethod
    def construct(
        cls, schedule: Schedule, current_user: User | None = None
    ) -> "ScheduleOut":
        return cls.model_validate(
            schedule.model_dump(),
            update={
                "is_finished_by_logged_in_user": False,
                "passages": schedule.passages,
            },
            context={"user": current_user, "finished_users": schedule.finished_users},
        )

    @field_validator("is_finished_by_logged_in_user", mode="before")
    def determine_finished_by_user(cls, value: bool, info: FieldValidationInfo) -> bool:
        if (context := info.context) and (user := context.get("user")):
            finished_users = context.get("finished_users", [])
            return user in finished_users
        return False
