from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.auth import AuthCode, AuthCodeCreate, AuthCodeUpdate
from app.models.user import User


class CRUDAuthCode(CRUDBase[AuthCode, AuthCodeCreate, AuthCodeUpdate]):
    async def get_by_user(self, session: AsyncSession, user: User) -> AuthCode | None:
        query = select(self.model).where(self.model.user == user)
        result = await session.exec(query)
        return result.first()

    async def get_by_code(
        self, session: AsyncSession, code: str | None
    ) -> AuthCode | None:
        query = select(self.model).where(self.model.code == code)
        result = await session.exec(query)
        return result.first()

    async def create_for_user(self, session: AsyncSession, user: User) -> AuthCode:
        if auth_code := await self.get_by_user(session, user):
            await self.delete(session, auth_code)

        return await self.create(session, AuthCodeCreate(user_id=user.id))


auth_code = CRUDAuthCode(AuthCode)
