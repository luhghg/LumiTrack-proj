
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from scr.models.bd_models import Course



async def create_course(session: AsyncSession, course_data: Course) -> Course:
    session.add(course_data)
    await session.commit()
    await session.refresh(course_data)
    return course_data

async def get_course_by_id(session: AsyncSession, course_id: int):
    query = (
        select(Course)
        .where(Course.id == course_id)       
            )
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def get_all_courses(session: AsyncSession, offset: int, limit: int) -> list[Course]:
    query= (
        select(Course)
        .offset(offset)
        .limit(limit)
    )
    result = await session.execute(query)
    return result.scalars().all()

