from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from scr.db.session import get_session
from scr.schemas.mentorship_schemas import MentorshipResponse, MentorshipCreate
from scr.models.bd_models import User
from scr.core.security import get_current_user
from scr.services.mentorship_service import send_request, respond_to_request

router =  APIRouter(prefix="/mentorship", tags=["mentorship"])

@router.post("/request", response_model=MentorshipResponse)
async def send_request_endpoint(request_data: MentorshipCreate,
                                session: AsyncSession = Depends(get_session),
                                current_user: User = Depends(get_current_user)
                                ):
    res = await send_request(session=session, mentor_id=request_data.mentor_id, current_user=current_user)
    return res

@router.patch("/request/{request_id}", response_model=MentorshipResponse)
async def respond_to_request_endpoint(request_id: int,
                                    status: str,
                                    session: AsyncSession = Depends(get_session),
                                    current_user: User = Depends(get_current_user)
                                    ):
    res = await respond_to_request(session=session, request_id=request_id, status=status, current_user=current_user)
    return res