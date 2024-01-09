from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.main import app
from app.tests.utils.user import TEST_USER_EMAIL, TEST_USER_NAME, create_random_user
from app.tests.utils.utils import random_email, random_lower_string


async def test_get_users_superuser_me(
    client: AsyncClient, superuser_token_headers: dict[str, str]
) -> None:
    r = await client.get(
        app.url_path_for("read_current_user"), headers=superuser_token_headers
    )
    current_user = r.json()
    assert current_user
    assert current_user["email"] == TEST_USER_EMAIL
    assert current_user["display_name"] == TEST_USER_NAME
    assert current_user["is_active"] is True
    assert current_user["is_superuser"] is True
    assert current_user["is_admin"] is False


async def test_get_users_admin_user_me(
    client: AsyncClient, admin_user_token_headers: dict[str, str]
) -> None:
    r = await client.get(
        app.url_path_for("read_current_user"), headers=admin_user_token_headers
    )
    current_user = r.json()
    assert current_user
    assert current_user["email"] == TEST_USER_EMAIL
    assert current_user["display_name"] == TEST_USER_NAME
    assert current_user["is_active"] is True
    assert current_user["is_superuser"] is False
    assert current_user["is_admin"] is True


async def test_get_users_normal_user_me(
    client: AsyncClient, normal_user_token_headers: dict[str, str]
) -> None:
    r = await client.get(
        app.url_path_for("read_current_user"), headers=normal_user_token_headers
    )
    current_user = r.json()
    assert current_user
    assert current_user["email"] == TEST_USER_EMAIL
    assert current_user["display_name"] == TEST_USER_NAME
    assert current_user["is_active"] is True
    assert current_user["is_superuser"] is False
    assert current_user["is_admin"] is False


async def test_create_user_new_email(
    client: AsyncClient, superuser_token_headers: dict, session: AsyncSession
) -> None:
    data = {
        "email": random_email(),
        "password": random_lower_string(),
        "display_name": random_lower_string(),
    }
    r = await client.post(
        app.url_path_for("create_user"), headers=superuser_token_headers, json=data
    )
    assert r.status_code == status.HTTP_201_CREATED
    created_user = r.json()
    user = await crud.user.get_by_email(session, data["email"])
    assert user
    assert user.email == created_user["email"] == data["email"]


async def test_get_existing_user(
    client: AsyncClient, admin_user_token_headers: dict, session: AsyncSession
) -> None:
    user = await create_random_user(session)
    r = await client.get(
        app.url_path_for("read_user", user_id=user.id),
        headers=admin_user_token_headers,
    )
    assert r.status_code == status.HTTP_200_OK
    api_user = r.json()
    existing_user = await crud.user.get_by_email(session, email=user.email)
    assert existing_user
    assert existing_user.email == api_user["email"]


async def test_create_user_existing_email(
    client: AsyncClient, superuser_token_headers: dict, session: AsyncSession
) -> None:
    user = await create_random_user(session)
    data = {
        "email": user.email,
        "password": random_lower_string(),
        "display_name": random_lower_string(),
    }
    r = await client.post(
        app.url_path_for("create_user"), headers=superuser_token_headers, json=data
    )
    created_user = r.json()
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert "_id" not in created_user


async def test_create_user_by_normal_user(
    client: AsyncClient, normal_user_token_headers: dict[str, str]
) -> None:
    data = {
        "email": random_email(),
        "password": random_lower_string(),
        "display_name": random_lower_string(),
    }
    r = await client.post(
        app.url_path_for("create_user"), headers=normal_user_token_headers, json=data
    )
    assert r.status_code == status.HTTP_403_FORBIDDEN


async def test_retrieve_users(
    client: AsyncClient, admin_user_token_headers: dict, session: AsyncSession
) -> None:
    await create_random_user(session)
    await create_random_user(session)
    r = await client.get(
        app.url_path_for("read_users"), headers=admin_user_token_headers
    )
    all_users = r.json()
    assert len(all_users) > 1
    for user in all_users:
        assert "email" in user
