from pydantic import BaseModel, ConfigDict

class MentorshipCreate(BaseModel):
    mentor_id: int

class MentorshipResponse(BaseModel):
    id: int
    sender_id: int
    mentor_id: int
    status: str
    model_config = ConfigDict(from_attributes=True) 