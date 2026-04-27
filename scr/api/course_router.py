from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from scr.db.session import get_session
from scr.schemas.course_schemas import CourseCreate, CourseResponse, CourseListResponse
from scr.models.bd_models import User
from scr.core.security import get_current_user
from scr.services.course_service import create_course, get_course, get_courses



router =  APIRouter(prefix="/courses", tags=["courses"])


@router.post("/", response_model=CourseResponse)
async def create_course_endpoint(course: CourseCreate,
                                 session: AsyncSession = Depends(get_session),
                                 current_user: User = Depends(get_current_user)
                                 ):
    if current_user.role != "admin": 
        raise HTTPException(status_code=403, detail="Forbidden")
    return await create_course(session=session, course_data=course, current_user=current_user)


@router.get("/", response_model=CourseListResponse)
async def get_courses_endpoint(session: AsyncSession = Depends(get_session),
                               offset: int = 0,
                               limit: int = 10,
                               current_user: User = Depends(get_current_user) 
                               ):
    return await get_courses(session=session, offset=offset, limit=limit)


@router.get("/{course_id}", response_model = CourseResponse)
async def get_course_endpoint(course_id: int,
                              session: AsyncSession = Depends(get_session),
                              current_user: User = Depends(get_current_user),
                              ):
    return await get_course(session=session, course_id=course_id)


    

    

