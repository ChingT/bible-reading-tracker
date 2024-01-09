from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool, QueuePool
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import ModeEnum, settings

engine = create_async_engine(
    settings.ASYNC_DATABASE_URI,
    echo=settings.MODE != ModeEnum.production,
    future=True,
    # Asincio pytest works with NullPool
    poolclass=NullPool if settings.MODE == ModeEnum.testing else QueuePool,
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
