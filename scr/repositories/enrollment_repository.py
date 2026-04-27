from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from scr.models.bd_models import Enrollment

async def enroll(session: AsyncSession, user_id: int, course_id: int) -> Enrollment:
    enrollment = Enrollment(user_id=user_id, course_id=course_id)
    session.add(enrollment)
    await session.commit()
    await session.refresh(enrollment)
    return enrollment

async def get_enrollment(session: AsyncSession, user_id: int, course_id: int) -> Enrollment:
    query = (
        select(Enrollment)
        .where(Enrollment.user_id == user_id, Enrollment.course_id == course_id)
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def get_user_enrollments(session: AsyncSession, user_id: int) -> list[Enrollment]:
    query = (
        select(Enrollment)
        .where(Enrollment.user_id == user_id)
    )
    result = await session.execute(query)
    return result.scalars().all()


