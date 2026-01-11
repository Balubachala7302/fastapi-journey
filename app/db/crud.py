from sqlalchemy.orm import Session
from app.db import models
from app.core.security import verify_password, hash_password


# -------------------------------
# Create User
# -------------------------------
def create_user(
    db: Session,
    username: str,
    email: str,
    password: str,
    role: str = "user"
):
    user = models.User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


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