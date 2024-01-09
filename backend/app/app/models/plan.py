from sqlmodel import SQLModel

from .base_model import BaseUUIDModel


class Plan(BaseUUIDModel, table=True):
    title: str
    description: str


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
