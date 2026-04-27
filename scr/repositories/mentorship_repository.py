from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from scr.models.bd_models import MentorshipRequest


async def create_request(session: AsyncSession, sender_id: int, mentor_id: int) -> MentorshipRequest:
    mentorship_request = MentorshipRequest(sender_id=sender_id, mentor_id=mentor_id, status="pending")
    session.add(mentorship_request)
    await session.commit()
    await session.refresh(mentorship_request)
    return mentorship_request

async def get_request(session: AsyncSession, request_id: int) -> MentorshipRequest | None:
    query = (
        select(MentorshipRequest)
        .where(MentorshipRequest.id == request_id)
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def update_status(session: AsyncSession, request: MentorshipRequest, status: str) -> MentorshipRequest:
    request.status = status
    session.add(request)
    await session.commit()
    await session.refresh(request)
    return request