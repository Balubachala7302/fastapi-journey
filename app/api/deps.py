from app.db.database import get_db
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.core.redis import redis_client
from app.core.config import get_settings
from jose import JWTError, jwt

settings=get_settings()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
def get_current_user(token: str = Depends(oauth2_scheme)):
    if redis_client.exists(token):
        raise HTTPException(
            status_code=401,
            detail="Token has been revoked"
        )

    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return payload

def get_current_active_user(
    user = Depends(get_current_user)
):
    return user



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
