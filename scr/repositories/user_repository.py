
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from scr.models.bd_models import User



async def get_by_email(session: AsyncSession, email: str):
    query = (
        select(User)
        .where(User.email == email))
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def create(session: AsyncSession,user_data: User):
    session.add(user_data)
    await session.commit()
    await session.refresh(user_data)
    return user_data

async def get_by_id(session: AsyncSession, id: int):
    query = (
        select(User)
        .where(User.id == id))
    result = await session.execute(query)
    return result.scalar_one_or_none()

    



