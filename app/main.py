from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import engine, get_db
from app.db import models, crud
from app.core.config import settings
from app.core.security import create_access_token, get_current_user
from app.db.schemas import UserCreate,UserOut
from app.db.schemas import PostCreate,PostOut
from app.api import auth,users
from fastapi.responses import JSONResponse
from fastapi import Request

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, version="1.0.0",description="FastAPI backend with JWT authentication")

app.include_router(auth.router)
app.include_router(users.router)


# -------------------------------
# Schemas
# -------------------------------
class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    username: str
    email: str
    role: str


# -------------------------------
# Public Routes
# -------------------------------
@app.get("/")
def root():
    return {"message": "FastAPI 80/20 Journey Begins"}

@app.get("/health")
def health():
    return {"status": "OK", "service": "FastAPI"}


# -------------------------------
# Auth Routes (DB-backed)
# -------------------------------
@app.post("/register", response_model=UserOut)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return crud.create_user(db,user)


# -------------------------------
# Protected Routes
# -------------------------------
@app.get("/me", response_model=UserResponse)
def my_profile(user: models.User = Depends(get_current_user)):
    return {
        "username": user.username,
        "email": user.email,
        "role": user.role
    }

@app.post("/posts", response_model=PostOut)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud.create_post(
        db=db,
        title=post.title,
        content=post.content,
        owner_id=user.id
    )


@app.get("/posts/me", response_model=list[PostOut])
def my_posts(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud.get_posts_by_user(db, user.id)

@app.delete("/posts/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   # ✅ user injected
):
    post = crud.get_post_by_id(db, post_id)

    if not post:
        raise HTTPException(status_code=404,detail="Post Not Found")

    if post.owner_id != user.id and user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed"
        )
    crud.delete_post(db.post)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "path": request.url.path
        }
    )