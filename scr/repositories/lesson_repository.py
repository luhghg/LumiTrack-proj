from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from scr.schemas.lessons_schemas import LessonCreate, ModuleCreate
from scr.models.bd_models import Modul, Lesson


async def create_module(session: AsyncSession, course_id: int, module_data: ModuleCreate) -> Modul:
    module = Modul(course_id=course_id, title=module_data.title, order_index=module_data.order_index)
    session.add(module)
    await session.commit()
    await session.refresh(module)
    return module


async def get_modules(session: AsyncSession, course_id: int) -> list[Modul]:
    query = (
        select(Modul)
        .where(Modul.course_id == course_id)
        .order_by(Modul.order_index)
    )
    result = await session.execute(query)
    return result.scalars().all()


async def create_lesson(session: AsyncSession, module_id: int, lesson_data: LessonCreate) -> Lesson:
    lesson = Lesson(module_id=module_id, title=lesson_data.title, content=lesson_data.content)
    session.add(lesson)
    await session.commit()
    await session.refresh(lesson)
    return lesson


async def get_lessons(session: AsyncSession, module_id: int) -> list[Lesson]:
    query = (
        select(Lesson)
        .where(Lesson.module_id == module_id)
    )
    result = await session.execute(query)
    return result.scalars().all()