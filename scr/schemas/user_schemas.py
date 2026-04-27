from pydantic import BaseModel, EmailStr, ConfigDict, Field
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(max_length=72)
    full_name: str | None = None
    role: str = Field(default="user")

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str | None
    role: str
    is_active: bool
    created_at: datetime.datetime

    model_config =  ConfigDict(from_attributes=True)
    

class Token(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")


class LoginData(BaseModel):
    email: str
    password: str



