from fastapi import APIRouter, Depends

from scr.core.security import get_current_user
from scr.models.bd_models import User
from scr.schemas.user_schemas import UserResponse


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def get_current_user_endpoint(current_user: User = Depends(get_current_user)):
    return current_user


