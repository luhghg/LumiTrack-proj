from pydantic import BaseModel, ConfigDict

from datetime import datetime

class EnrollmentCreate(BaseModel):
    course_id: int

class EnrollmentResponse(BaseModel):
    user_id: int
    course_id: int
    enrolled_at: datetime
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)


