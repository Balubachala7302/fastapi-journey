from sqlalchemy.orm import Session
from app.db import models
from app.db.schemas import UserCreate
from app.core.security import hash_password,verify_password


def create_user(db: Session, user: UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        role="user"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# -------------------------------
# Get user by email
# -------------------------------
def get_user_by_email(db: Session, email: str):
    return (
        db.query(models.User)
        .filter(models.User.email == email)
        .first()
    )


# -------------------------------
# Authenticate user
# -------------------------------
def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    user = get_user_by_email(db, email)
    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user

def get_post_by_id(db:Session,post_id:int):
    return(
        db.query(models.Post)
        .filter(models.Post.id == post_id)
        .first()
    )

def create_post(
    db: Session,
    title: str,
    content: str,
    owner_id: int
):
    post = models.Post(
        title=title,
        content=content,
        owner_id=owner_id
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_posts_by_user(
    db: Session,
    user_id: int
):
    return (
        db.query(models.Post)
        .filter(models.Post.owner_id == user_id)
        .all()
    )

def delete_post(db:Session,post:models.Post):
    db.delete(post)
    db.commit()


def create_refresh_token(db,token:str,user_id:int):
    db_token=models.RefreshToken(
        token=token,
        user_id=user_id
    )
    db.add(db_token)
    db.commit()
    return db_token


def get_refresh_token(db,token:str):
    return (
        db.query(models.RefreshToken)
        .filter(models.RefreshToken.token==token)
        .first()
        )

def delete_refresh_token(db,token:str):
    db_token=get_refresh_token(db,token)
    if db_token:
        db.delete(db_token)
        db.commit()

def blacklist_token(db: Session, token: str):
    db_token = models.BlacklistedToken(token=token)
    db.add(db_token)
    db.commit()

def is_token_blacklisted(db: Session, token: str) -> bool:
    return db.query(models.BlacklistedToken)\
             .filter(models.BlacklistedToken.token == token)\
             .first() is not None