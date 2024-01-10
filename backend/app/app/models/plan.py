from typing import TYPE_CHECKING

from sqlmodel import Relationship, SQLModel

from .base_model import BaseUUIDModel

if TYPE_CHECKING:
    from .schedule import Schedule


class Plan(BaseUUIDModel, table=True):
    title: str
    description: str

    schedules: list["Schedule"] = Relationship(back_populates="plan")


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
