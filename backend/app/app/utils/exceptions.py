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
