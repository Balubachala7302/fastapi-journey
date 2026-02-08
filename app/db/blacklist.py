# app/db/blacklist.py

from sqlalchemy.orm import Session
from app.db import models
from datetime import datetime


def blacklist_token(db: Session, token: str):
    db_token = models.BlacklistedToken(
        token=token,
        blacklisted_at=datetime.utcnow()
    )
    db.add(db_token)
    db.commit()


def is_token_blacklisted(db: Session, token: str) -> bool:
    return (
        db.query(models.BlacklistedToken)
        .filter(models.BlacklistedToken.token == token)
        .first()
        is not None
    )