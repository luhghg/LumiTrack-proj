from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from scr.db.session import get_session
from scr.schemas.enrollment_schemas import EnrollmentResponse
from scr.models.bd_models import User
from scr.core.security import get_current_user
from scr.services.enrollment_service import enroll_user, get_my_courses

router =  APIRouter(prefix="/enrollments", tags=["enrollments"])

@router.get("/my", response_model=list[EnrollmentResponse])
async def get_my_courses_endpoint(session: AsyncSession  = Depends(get_session),
                                  current_user: User = Depends(get_current_user)
                                  ):
    return await get_my_courses(session=session, current_user=current_user)


@router.post("/{course_id}", response_model=EnrollmentResponse)
async def enroll_course_endpoint(course_id: int,
                                 session: AsyncSession = Depends(get_session),
                                 current_user: User = Depends(get_current_user)
                                 ):
    return await enroll_user(session=session, course_id=course_id, current_user=current_user)

