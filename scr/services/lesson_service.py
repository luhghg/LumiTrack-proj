from sqlalchemy.ext.asyncio import AsyncSession
from scr.models.bd_models import  Lesson, Modul, User
from scr.repositories.course_repository import get_course_by_id
from scr.repositories.lesson_repository import create_lesson, create_module, get_lessons, get_modules
from scr.schemas.lessons_schemas import LessonCreate, ModuleCreate
from fastapi import HTTPException

async def add_module(session: AsyncSession, course_id: int, module_data: ModuleCreate, current_user: User) -> Modul:
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    course = await get_course_by_id(session=session, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    module = await create_module(session=session, course_id=course_id, module_data=module_data)
    return module
    

async def get_course_modules(session: AsyncSession, course_id: int) -> list[Modul]:
    modul = await get_modules(session=session, course_id=course_id)
    return modul


async def add_lesson(session: AsyncSession, module_id: int, lesson_data: LessonCreate, current_user: User) -> Lesson:
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    module = await create_lesson(session=session, module_id=module_id, lesson_data=lesson_data)
    return module


async def get_modul_lessons(session: AsyncSession, module_id: int) -> list[Lesson]:
    lessons = await get_lessons(session=session, module_id=module_id)
    return lessons