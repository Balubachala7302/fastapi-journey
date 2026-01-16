from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY,ALGORITHM
from app.core.security import create_access_token
from app.db.database import get_db
from app.db import crud
from jose import JWTError,jwt
from app.db.schemas import TokenResponse
from app.core.security import create_access_token, create_refresh_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate user and return JWT token
    """
    user = crud.authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }




@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = crud.authenticate_user(
        db,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    refresh_token = create_refresh_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh")
def refresh_token(
    refresh_token: str,
    db: Session = Depends(get_db)
):
    db_token = crud.get_refresh_token(db, refresh_token)
    if not db_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")

    access_token = create_access_token({"sub": email})

    return {"access_token": access_token}

@router.post("/logout")
def logout(refresh_token: str, db: Session = Depends(get_db)):
    crud.delete_refresh_token(db, refresh_token)
    return {"message": "Logged out successfully"}