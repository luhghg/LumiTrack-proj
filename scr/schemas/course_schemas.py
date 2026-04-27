from pydantic import BaseModel, ConfigDict


class CourseCreate(BaseModel):
    title: str
    description: str |  None = None


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str | None
    creator_id: int

    model_config = ConfigDict(from_attributes=True)  
            # - дає читати данні з обєкта тип ось так CourseResponce.id а не тільки з дікт

class CourseListResponse(BaseModel):

    courses: list[CourseResponse]
    total: int