from sqlalchemy.ext.asyncio import AsyncSession
from scr.schemas.user_schemas import UserCreate, Token
from scr.models.bd_models import User
from fastapi import HTTPException
from scr.repositories.user_repository import get_by_email, create
from scr.core.security import hash_password, verify_password, create_access_token



async def register_user(session:AsyncSession, user_data: UserCreate) -> User:
    if await get_by_email(session=session, email=user_data.email) is not None:
        raise HTTPException(status_code=400, detail= " Email already registered")
    hash_pass = hash_password(user_data.password)
    new_user  = User(full_name = user_data.full_name, role = user_data.role, email = user_data.email, hashed_password = hash_pass)
    create_new_user = await create(session, new_user)
    return create_new_user

async def login_user(session: AsyncSession, email: str, password: str) -> Token:
    user = await get_by_email(session=session, email=email)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if verify_password(password, user.hashed_password) == False:
        raise HTTPException(status_code = 401, detail= "Invalid credentials")
    token = create_access_token({"sub": str(user.id), "role": user.role})
    return Token(access_token=token, token_type="bearer")
    
    
    
        
    


    
    



    
    

