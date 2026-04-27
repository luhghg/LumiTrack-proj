from sqlalchemy.ext.asyncio import AsyncSession
from scr.models.bd_models import MentorshipRequest, User
from scr.repositories.user_repository import get_by_id
from scr.repositories.mentorship_repository import create_request, get_request, update_status
from fastapi import HTTPException

async def send_request(session: AsyncSession, mentor_id: int, current_user: User) -> MentorshipRequest:
    if mentor_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot send request to yourself")
    mentor = await get_by_id(session=session, user_id=mentor_id)
    if mentor is None:
        raise HTTPException(status_code=404, detail="Mentor not found")
    res = await create_request(session=session, sender_id= current_user.id, mentor_id=mentor_id)
    return res


async def respond_to_request(session:AsyncSession, request_id: int, status: str, current_user: User) -> MentorshipRequest:
    get_req = await get_request(session=session, request_id = request_id)
    if get_req is None:
        raise HTTPException(status_code=404, detail="Request not found")
    if get_req.mentor_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to respond to this request")
    if status not in ["accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    res = await update_status(session=session, request=get_req, status=status)
    return res




