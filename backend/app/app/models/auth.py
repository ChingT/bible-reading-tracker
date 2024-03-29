from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.utils.utils import code_generator

from .base_model import BaseModel

if TYPE_CHECKING:
    from .user import User


class CodeType(Enum):
    ACCESS = "access"
    REFRESH = "refresh"
    REGISTER = "register"
    PASSWORD_RESET = "password-reset"


class VerifyAccessTokenRequest(SQLModel):
    access_token: str


class RefreshTokenRequest(SQLModel):
    refresh_token: str


class TokensResponse(SQLModel):
    token_type: str = "bearer"
    access_token: str
    refresh_token: str


class JWTTokenPayload(SQLModel):
    sub: str
    exp: datetime
    nbf: datetime
    code_type_value: str


class NewPassword(SQLModel):
    token: str
    new_password: str


class AuthCode(BaseModel, table=True):
    code: str = Field(unique=True, default_factory=code_generator)
    is_used: bool = False

    user_id: UUID = Field(unique=True, foreign_key="user.id")
    user: "User" = Relationship(
        back_populates="auth_code", sa_relationship_kwargs={"lazy": "subquery"}
    )


class AuthCodeCreate(SQLModel):
    user_id: UUID


class AuthCodeUpdate(SQLModel):
    pass
