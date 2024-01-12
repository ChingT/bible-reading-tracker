from collections.abc import AsyncGenerator
from typing import Annotated
from uuid import UUID

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel.ext.asyncio.session import AsyncSession

from app.api.exceptions import (
    credentials_exception,
    get_or_404,
    inactive_user_exception,
    no_permissions_exception,
)
from app.core.token_utils import CodeType, decode_token
from app.db.session import SessionLocal
from app.models.plan import Plan
from app.models.schedule import Schedule
from app.models.user import User


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="auth/access-token")
TokenDep = Annotated[str, Depends(reusable_oauth2)]
FormDataDep = Annotated[OAuth2PasswordRequestForm, Depends()]


async def get_current_user(session: SessionDep, token: TokenDep) -> User:
    if user_id := decode_token(token, CodeType.ACCESS):
        user = await get_user_or_404(session, UUID(user_id))
        if not user.is_active:
            raise inactive_user_exception
        return user
    raise credentials_exception


async def get_current_admin_superuser(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    if not current_user.is_superuser and not current_user.is_admin:
        raise no_permissions_exception
    return current_user


async def get_user_or_404(session: SessionDep, user_id: UUID) -> User:
    return await get_or_404(session, User, user_id)


async def get_schedule_or_404(session: SessionDep, schedule_id: UUID) -> Schedule:
    return await get_or_404(session, Schedule, schedule_id)


async def get_plan_or_404(session: SessionDep, plan_id: UUID) -> Plan:
    return await get_or_404(session, Plan, plan_id)


CurrentUser = Annotated[User, Depends(get_current_user)]
AdminSuperuser = Annotated[User, Depends(get_current_admin_superuser)]

UserDep = Annotated[User, Depends(get_user_or_404)]
ScheduleDep = Annotated[Schedule, Depends(get_schedule_or_404)]
PlanDep = Annotated[Plan, Depends(get_plan_or_404)]
