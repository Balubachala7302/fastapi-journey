from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db import crud
from app.db.schemas import UserCreate

def register_user(db: Session, user: UserCreate):
    existing_user = crud.get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return crud.create_user(db, user)