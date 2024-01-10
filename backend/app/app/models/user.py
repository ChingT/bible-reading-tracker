from pydantic import EmailStr
from sqlmodel import Column, Field, Relationship, SQLModel, String

from .auth import AuthCode
from .base_model import BaseModel
from .user_schedule_link import UserScheduleLink


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
    finished_schedule_links: list[UserScheduleLink] = Relationship(
        back_populates="user"
    )


class UserCreate(SQLModel):
    email: EmailStr
    password: str
    display_name: str


class UserUpdate(SQLModel):
    display_name: str


class UserUpdatePassword(SQLModel):
    password: str


class UserRecoverPassword(SQLModel):
    email: EmailStr


class UserOut(UserBase):
    pass
