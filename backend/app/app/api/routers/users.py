from typing import Any

from fastapi import APIRouter, Depends, Query, status

from app import crud
from app.api.deps import CurrentUser, SessionDep, get_current_admin_superuser
from app.api.exceptions import email_registered_exception, user_not_found_exception
from app.models.user import UserCreateFromUser, UserOut, UserUpdateFromUser

router = APIRouter()


@router.get("/me", response_model=UserOut)
async def read_current_user(current_user: CurrentUser) -> Any:
    """Get current user."""
    return current_user


@router.patch("/me", response_model=UserOut)
async def update_current_user(
    session: SessionDep, current_user: CurrentUser, updated_data: UserUpdateFromUser
) -> Any:
    """Update current user."""
    return await crud.user.update_from_user(session, current_user, updated_data)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_current_user(session: SessionDep, current_user: CurrentUser):
    """Delete current user."""
    await crud.user.delete(session, current_user)
    return {"msg": "User deleted"}


@router.post(
    "/",
    dependencies=[Depends(get_current_admin_superuser)],
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
)
async def create_user(session: SessionDep, user: UserCreateFromUser) -> Any:
    """Only superuser can perform this operation."""
    if await crud.user.get_by_email(session, user.email):
        raise email_registered_exception
    return await crud.user.create_from_user(session, user)


@router.get(
    "/",
    dependencies=[Depends(get_current_admin_superuser)],
    response_model=list[UserOut],
)
async def read_users(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> Any:
    return await crud.user.list(session, offset, limit)


@router.get(
    "/{user_id}",
    dependencies=[Depends(get_current_admin_superuser)],
    response_model=UserOut,
)
async def read_user(session: SessionDep, user_id: int) -> Any:
    db_obj = await crud.user.get(session, id=user_id)
    if db_obj is None:
        raise user_not_found_exception
    return db_obj
