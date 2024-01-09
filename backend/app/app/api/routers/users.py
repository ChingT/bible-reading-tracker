from fastapi import APIRouter, Depends, Query, status

from app import crud
from app.api.deps import CurrentUser, SessionDep, get_current_admin_superuser
from app.api.utils import email_registered_exception, user_not_found_exception
from app.models.user import UserCreate, UserOut, UserUpdate

router = APIRouter()


@router.get("/me")
async def read_current_user(current_user: CurrentUser) -> UserOut:
    """Get current user."""
    return current_user


@router.patch("/me")
async def update_current_user(
    session: SessionDep, current_user: CurrentUser, updated_data: UserUpdate
) -> UserOut:
    """Update current user."""
    return await crud.user.update(session, current_user, updated_data)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_current_user(session: SessionDep, current_user: CurrentUser):
    """Delete current user."""
    await crud.user.delete(session, current_user)
    return {"msg": "User deleted"}


@router.post(
    "/",
    dependencies=[Depends(get_current_admin_superuser)],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(session: SessionDep, user: UserCreate) -> UserOut:
    """Only superuser can perform this operation."""
    if await user.get_by_email(session, user.email):
        raise email_registered_exception
    return await user.create(session, user)


@router.get("/", dependencies=[Depends(get_current_admin_superuser)])
async def read_users(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
) -> list[UserOut]:
    return await crud.user.list(session, offset, limit)


@router.get("/{user_id}", dependencies=[Depends(get_current_admin_superuser)])
async def read_user(session: SessionDep, user_id: int) -> UserOut:
    db_obj = await crud.user.get(session, user_id)
    if db_obj is None:
        raise user_not_found_exception
    return db_obj
