from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from scr.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from scr.db.session import get_session
from scr.models.bd_models import User
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from scr.repositories.user_repository import get_by_id

oauth2_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict)-> str :
    to_encode = data.copy()
    exp = datetime.now(timezone.utc) + timedelta(minutes=20)
    to_encode.update({"exp": exp})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

async def get_current_user(session: AsyncSession = Depends(get_session), credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    func_get_id = await get_by_id(session, int(user_id))
    if func_get_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return func_get_id
