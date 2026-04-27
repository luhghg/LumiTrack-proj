from sqlalchemy.ext.asyncio import AsyncSession
from scr.models.bd_models import User, Enrollment
from scr.repositories.course_repository import get_course_by_id
from scr.repositories.enrollment_repository import enroll, get_enrollment, get_user_enrollments
from fastapi import HTTPException

async def enroll_user(session: AsyncSession, course_id: int, current_user: User) -> Enrollment:
    course = await get_course_by_id(session=session, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail=" Course not found")
    chek = await get_enrollment(session=session, user_id=current_user.id, course_id=course_id)
    if chek is not None:
        raise HTTPException(status_code=400, detail="Already enrolled")
    enrolll = await enroll(session=session, user_id = current_user.id, course_id=course_id)
    return enrolll

async def get_my_courses(session : AsyncSession, current_user: User) -> list[Enrollment]:
    enrill = await get_user_enrollments(session=session, user_id=current_user.id)
    return enrill

    


