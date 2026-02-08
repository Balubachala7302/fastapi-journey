from app.db.database import get_db
from app.core.security import get_current_user
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

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
