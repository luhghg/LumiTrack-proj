from sqlalchemy.ext.asyncio import AsyncSession
from scr.schemas.course_schemas import CourseCreate, CourseListResponse
from scr.models.bd_models import User, Course
from scr.repositories.course_repository import create_course as create_course_repo, get_course_by_id, get_all_courses
from fastapi import HTTPException

async def create_course(session: AsyncSession, course_data: CourseCreate, current_user: User)-> Course:
    course = Course(title=course_data.title, description=course_data.description, creator_id= current_user.id)
    cnc = await create_course_repo(session, course)
    return cnc

async def get_course(session: AsyncSession, course_id: int) -> Course:
    course_by_id = await get_course_by_id(session, course_id)
    if course_by_id is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_by_id

async def get_courses(session: AsyncSession, offset: int = 0, limit: int = 10) -> CourseListResponse:
    courses = await get_all_courses(session, offset, limit)
    all_courses = CourseListResponse(courses=courses, total=len(courses))
    return all_courses







