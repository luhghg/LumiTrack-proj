from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from scr.db.session import get_session
from scr.schemas.lessons_schemas import LessonCreate, LessonResponse, ModuleCreate, ModuleResponse
from scr.models.bd_models import User
from scr.core.security import get_current_user

from scr.services.lesson_service import add_module, get_course_modules, add_lesson, get_modul_lessons

router =  APIRouter(prefix="/lessons", tags=["lessons"])

@router.post("/courses/{course_id}/modules", response_model=ModuleResponse)
async def create_module(
    course_id: int,
    module_data: ModuleCreate,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return await add_module(session=session, course_id=course_id, module_data=module_data, current_user=current_user)


@router.get("/courses/{course_id}/modules", response_model=list[ModuleResponse])
async def get_modules(
    course_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await get_course_modules(session=session, course_id=course_id)


@router.post("/modules/{module_id}/lessons", response_model=LessonResponse)
async def create_lesson(
    module_id: int,
    lesson_data: LessonCreate,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return await add_lesson(session=session, module_id=module_id, lesson_data=lesson_data, current_user=current_user)


@router.get("/modules/{module_id}/lessons", response_model=list[LessonResponse])
async def get_lessons(
    module_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await get_modul_lessons(session=session, module_id=module_id)

