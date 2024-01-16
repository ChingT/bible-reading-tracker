from collections.abc import Sequence
from typing import Any, Generic, TypeVar

from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        """CRUD object with default methods to create, read, update, delete and list.

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def list(
        self, session: AsyncSession, offset: int = 0, limit: int = 100
    ) -> Sequence[ModelType]:
        query = select(self.model).offset(offset).limit(limit)
        result = await session.exec(query)
        return result.all()

    async def get(self, session: AsyncSession, **primary_kwargs) -> ModelType | None:
        return await session.get(self.model, primary_kwargs)

    async def get_by_attr(self, session: AsyncSession, **kwargs) -> ModelType | None:
        whereclauses = [
            getattr(self.model, key) == value for key, value in kwargs.items()
        ]
        query = select(self.model).where(*whereclauses)
        result = await session.exec(query)
        return result.first()

    async def create(
        self, session: AsyncSession, obj_in: CreateSchemaType
    ) -> ModelType:
        db_obj = self.model.model_validate(obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        session: AsyncSession,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any],
    ) -> ModelType:
        if isinstance(obj_in, dict):
            obj_data = obj_in
        else:
            obj_data = obj_in.model_dump(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, session: AsyncSession, db_obj: ModelType) -> ModelType:
        await session.delete(db_obj)
        await session.commit()
        return db_obj
