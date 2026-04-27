from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from scr.db.session import get_session
from scr.schemas.user_schemas import UserCreate, UserResponse, Token, LoginData
from scr.services.auth_service import register_user, login_user


router =  APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    result = await register_user(session, user_data)
    return result

@router.post("/login", response_model=Token)
async def login(login_data: LoginData, session: AsyncSession = Depends(get_session)):
    res = await login_user(session, login_data.email, login_data.password)
    return res


