from fastapi import FastAPI, Depends, HTTPException, status, Request, Query, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from math import ceil
import time

from app.db.database import engine, get_db
from app.db import models, crud
from app.db.schemas import (
    PaginatedPostResponse,
    UserCreate,
    UserOut,
    PostCreate,
    PostOut
)

from app.api import auth, users
from app.api.deps import get_current_user

from app.core.config import get_settings
from app.core.response import success_response, error_response
from app.core.logger import logger

from app.tasks import send_email_task


# -------------------------------
# DB Setup
# -------------------------------
models.Base.metadata.create_all(bind=engine)

settings = get_settings()


# -------------------------------
# FastAPI App
# -------------------------------
app = FastAPI(
    title="FastAPI Production Backend",
    version="1.0.0",
    description="""
    Production-ready FastAPI backend with:

    - JWT Authentication
    - Refresh Tokens
    - Redis Token Blacklisting
    - Role-Based Access Control
    - Service Layer Architecture
    - Structured Logging
    - Global Exception Handling
    """,
    contact={
        "name": "Bala Bhaskar",
        "email": "BalaBhaskar@gmail.com",
    },
)


# -------------------------------
# Startup / Shutdown Events
# -------------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 FastAPI application starting...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 FastAPI application shutting down...")


# -------------------------------
# Request Logging Middleware
# -------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round(time.time() - start_time, 4)

    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Time: {process_time}s"
    )

    return response


# -------------------------------
# Global Exception Handlers
# -------------------------------
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return error_response(
        message=exc.detail,
        status_code=exc.status_code
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return error_response(
        message="Validation Error",
        status_code=422
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"Unhandled error on {request.method} {request.url.path}: {str(exc)}"
    )

    return error_response(
        message="Internal Server Error",
        status_code=500
    )


# -------------------------------
# Include Routers
# -------------------------------
app.include_router(auth.router)
app.include_router(users.router)


# -------------------------------
# Public Routes
# -------------------------------
@app.get("/")
def root():
    return {"message": "FastAPI Advanced Backend Running 🚀"}


@app.get("/health")
def health():
    return {"status": "OK", "service": settings.APP_NAME}


# -------------------------------
# Protected Routes
# -------------------------------
@app.get("/me", response_model=UserOut)
def my_profile(user: models.User = Depends(get_current_user)):
    return user


@app.post("/posts", response_model=PostOut)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    return crud.create_post(
        db=db,
        title=post.title,
        content=post.content,
        owner_id=user.id
    )


@app.get(
    "/posts/me",
    response_model=PaginatedPostResponse,
    summary="Get My Posts (Paginated + Sorted)"
)
def my_posts(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    title: str | None = None,
    sort: str = Query("id"),
    order: str = Query("desc"),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):

    total, posts = crud.get_posts_by_user_paginated(
        db=db,
        user_id=user.id,
        page=page,
        limit=limit,
        title=title,
        sort=sort,
        order=order
    )

    total_pages = ceil(total / limit) if total > 0 else 1

    return success_response(
        data={
            "meta": {
                "total": total,
                "page": page,
                "limit": limit,
                "total_pages": total_pages
            },
            "items": posts
        },
        message="Posts fetched successfully"
    )


@app.delete("/posts/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):

    post = crud.get_post_by_id(db, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post Not Found"
        )

    if post.owner_id != user.id and user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed"
        )

    crud.delete_post(db, post_id)

    return {"message": "Post deleted successfully"}


# -------------------------------
# Background Task Example
# -------------------------------
@app.get("/send-email/background")
def send_email_background(background_tasks: BackgroundTasks):

    def fake_email():
        print("Sending email...")

    background_tasks.add_task(fake_email)

    return {"message": "Email will be sent in background"}


# -------------------------------
# Celery Task Example
# -------------------------------
@app.post("/send-email")
def send_email(email: str):

    send_email_task.delay(email)

    return {"message": "Email task queued"}