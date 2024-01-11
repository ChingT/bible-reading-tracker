from typing import Any, Generic, TypeVar
from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import SQLModel

ModelType = TypeVar("ModelType", bound=SQLModel)


class IdNotFoundException(HTTPException, Generic[ModelType]):
    def __init__(
        self, model: type[ModelType], id: UUID, headers: dict[str, Any] | None = None
    ) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unable to find the {model.__name__} with id {id}.",
            headers=headers,
        )


class NameNotFoundException(HTTPException, Generic[ModelType]):
    def __init__(
        self, model: type[ModelType], name: str, headers: dict[str, Any] | None = None
    ) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unable to find the {model.__name__} with name {name}.",
            headers=headers,
        )


credentials_exception = HTTPException(
    status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


no_permissions_exception = HTTPException(
    status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
)


user_not_found_exception = HTTPException(
    status.HTTP_404_NOT_FOUND, detail="User not found"
)
inactive_user_exception = HTTPException(
    status.HTTP_400_BAD_REQUEST, detail="Inactive user"
)
active_user_exception = HTTPException(
    status.HTTP_400_BAD_REQUEST, detail="User account already activated"
)
email_registered_exception = HTTPException(
    status.HTTP_400_BAD_REQUEST, detail="Email already registered"
)
