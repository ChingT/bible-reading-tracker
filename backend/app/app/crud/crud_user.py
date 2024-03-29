from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import (
    User,
    UserCreate,
    UserCreateFromUser,
    UserUpdate,
    UserUpdateFromUser,
    UserUpdatePassword,
)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, session: AsyncSession, email: str) -> User | None:
        query = select(self.model).where(self.model.email == email)
        result = await session.exec(query)
        return result.first()

    async def create_from_user(
        self,
        session: AsyncSession,
        obj_in: UserCreateFromUser,
        is_admin: bool = False,
        is_superuser: bool = False,
    ) -> User:
        db_obj = UserCreate(
            email=obj_in.email,
            display_name=obj_in.display_name,
            hashed_password=get_password_hash(obj_in.password),
            is_admin=is_admin,
            is_superuser=is_superuser,
        )
        return await self.create(session, obj_in=db_obj)

    async def update_from_user(
        self,
        session: AsyncSession,
        db_obj: User,
        obj_in: UserUpdateFromUser | UserUpdatePassword,
    ) -> User:
        obj_data = obj_in.model_dump(exclude_unset=True)
        if password := obj_data.get("password"):
            hashed_password = get_password_hash(password)
            del obj_data["password"]
            obj_data["hashed_password"] = hashed_password
        return await self.update(session, db_obj=db_obj, obj_in=obj_data)

    async def authenticate(
        self, session: AsyncSession, email: str, password: str
    ) -> User | None:
        user = await self.get_by_email(session, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def activate(self, session: AsyncSession, db_obj: User) -> bool:
        db_obj.is_active = True
        session.add(db_obj)
        await session.commit()
        return True


user = CRUDUser(User)
