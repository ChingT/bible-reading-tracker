import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Column, Field, Relationship, SQLModel, String

from .auth import AuthCode
from .base_model import BaseModel

if TYPE_CHECKING:
    from .schedule import Schedule


class UserScheduleLink(SQLModel, table=True):
    __tablename__ = "user_schedule_link"

    user_id: UUID = Field(foreign_key="user.id", primary_key=True)
    finished_schedule_id: UUID = Field(foreign_key="schedule.id", primary_key=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)


class UserBase(SQLModel):
    email: EmailStr = Field(sa_column=Column(String, index=True, unique=True))
    is_active: bool = False
    is_admin: bool = False
    is_superuser: bool = False
    display_name: str | None = None

    def __str__(self):
        return f"User {self.display_name}"


class User(BaseModel, UserBase, table=True):
    hashed_password: str

    auth_code: AuthCode = Relationship(
        back_populates="user", sa_relationship_kwargs={"cascade": "all, delete"}
    )
    finished_schedules: list["Schedule"] = Relationship(
        back_populates="finished_users",
        link_model=UserScheduleLink,
        sa_relationship_kwargs={"cascade": "all, delete"},
    )


class UserCreateFromUser(SQLModel):
    email: EmailStr
    password: str
    display_name: str


class UserCreate(SQLModel):
    email: EmailStr
    display_name: str
    hashed_password: str
    is_admin: bool
    is_superuser: bool


class UserUpdate(SQLModel):
    display_name: str | None = None
    hashed_password: str | None = None


class UserUpdateFromUser(SQLModel):
    display_name: str


class UserUpdatePassword(SQLModel):
    password: str


class UserRecoverPassword(SQLModel):
    email: EmailStr


class UserOut(BaseModel, UserBase):
    pass
