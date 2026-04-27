from pydantic import BaseModel, ConfigDict

class ModuleCreate(BaseModel):
    title: str
    order_index: int

class ModuleResponse(BaseModel):
    id: int
    title: str
    order_index: int
    course_id: int

    model_config = ConfigDict(from_attributes=True)

class LessonCreate(BaseModel):
    title: str
    content: str | None = None


class LessonResponse(BaseModel):
    id: int
    title: str
    content: str | None
    module_id: int

    model_config = ConfigDict(from_attributes=True)