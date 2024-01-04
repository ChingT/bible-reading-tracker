from fastapi import status
from httpx import AsyncClient

from app.main import app
from app.models.user import User
from app.tests.utils.user import TEST_USER_EMAIL, TEST_USER_PASSWORD


async def test_get_access_token(client: AsyncClient, superuser: User) -> None:
    login_data = {
        "username": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
    }
    r = await client.post(app.url_path_for("login_access_token"), data=login_data)
    tokens = r.json()
    assert r.status_code == status.HTTP_200_OK
    assert tokens["access_token"]
