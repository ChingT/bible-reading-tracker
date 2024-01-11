from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.core.config import settings
from app.core.token_utils import CodeType, create_token
from app.models.user import User, UserCreateFromUser
from app.tests.utils.utils import random_email, random_lower_string

TEST_USER_EMAIL = "test@example.com"
TEST_USER_PASSWORD = "1234"
TEST_USER_NAME = "test_user"


async def create_test_user(
    session: AsyncSession,
    is_admin: bool = False,
    is_superuser: bool = False,
    activate=True,
) -> User:
    user_in = UserCreateFromUser(
        email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD, display_name=TEST_USER_NAME
    )
    user = await crud.user.create_from_user(
        session, user_in, is_admin=is_admin, is_superuser=is_superuser
    )
    if activate:
        await crud.user.activate(session, user)
    return user


async def create_random_user(
    session: AsyncSession,
    is_admin: bool = False,
    is_superuser: bool = False,
    activate=True,
) -> User:
    user_in = UserCreateFromUser(
        email=random_email(),
        password=random_lower_string(),
        display_name=random_lower_string(),
    )
    user = await crud.user.create_from_user(
        session, user_in, is_admin=is_admin, is_superuser=is_superuser
    )
    if activate:
        await crud.user.activate(session, user)
    return user


async def get_user_authentication_headers(user: User) -> dict[str, str]:
    access_token = create_token(
        str(user.id), settings.ACCESS_TOKEN_EXPIRE_HOURS, CodeType.ACCESS
    )
    return {"Authorization": f"Bearer {access_token}"}
