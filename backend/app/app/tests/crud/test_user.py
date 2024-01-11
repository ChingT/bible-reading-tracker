from fastapi.encoders import jsonable_encoder
from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.core.security import verify_password
from app.models.user import UserUpdatePassword
from app.tests.utils.user import (
    TEST_USER_EMAIL,
    TEST_USER_NAME,
    TEST_USER_PASSWORD,
    create_random_user,
    create_test_user,
)
from app.tests.utils.utils import random_email, random_lower_string


async def test_create_user(session: AsyncSession) -> None:
    user = await create_test_user(session)
    assert user.email == TEST_USER_EMAIL
    assert user.display_name == TEST_USER_NAME
    assert hasattr(user, "hashed_password")
    assert not hasattr(user, "password")


async def test_authenticate_user(session: AsyncSession) -> None:
    await create_test_user(session)
    authenticated_user = await crud.user.authenticate(
        session, TEST_USER_EMAIL, TEST_USER_PASSWORD
    )
    assert authenticated_user
    assert authenticated_user.email == TEST_USER_EMAIL


async def test_not_authenticate_user(session: AsyncSession) -> None:
    email = random_email()
    password = random_lower_string()
    authenticated_user = await crud.user.authenticate(session, email, password)
    assert authenticated_user is None


async def test_check_if_user_is_active(session: AsyncSession) -> None:
    user = await create_random_user(session, activate=True)
    assert user.is_active is True


async def test_check_if_user_is_inactive(session: AsyncSession) -> None:
    user = await create_random_user(session, activate=False)
    assert user.is_active is False


async def test_check_if_user_is_admin(session: AsyncSession) -> None:
    user = await create_random_user(session, is_admin=True)
    assert user.is_admin is True
    assert user.is_superuser is False


async def test_check_if_user_is_superuser(session: AsyncSession) -> None:
    user = await create_random_user(session, is_superuser=True)
    assert user.is_admin is False
    assert user.is_superuser is True


async def test_check_if_user_is_normal_user(session: AsyncSession) -> None:
    user = await create_random_user(session)
    assert user.is_admin is False
    assert user.is_superuser is False


async def test_get_user(session: AsyncSession) -> None:
    user = await create_random_user(session)
    user_2 = await crud.user.get(session, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


async def test_update_user(session: AsyncSession) -> None:
    user = await create_random_user(session)
    new_password = random_lower_string()
    user_in_update = UserUpdatePassword(password=new_password)
    await crud.user.update_from_user(session, user, user_in_update)
    user_2 = await crud.user.get(session, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert verify_password(new_password, user_2.hashed_password)
