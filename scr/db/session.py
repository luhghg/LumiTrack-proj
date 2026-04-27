from sqlalchemy.orm import  sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from typing import AsyncGenerator

from scr.core.config import settings

async_engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        


