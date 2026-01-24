from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

    posts = relationship(
        "Post",
        back_populates="owner",
        cascade="all, delete"
    )


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship(
        "User",
        back_populates="posts"
    )

class RefreshToken(Base):
    __tablename__="refresh_tokens"
    id=Column(Integer,primary_key=True,index=True)
    token=Column(String,unique=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    created_at=Column(DateTime,default=datetime.utcnow)

    user=relationship("User")


class BlacklistedToken(Base):
     __tablename__="blacklisted_tokens"
     id=Column(Integer,primary_key=True,index=True)
     token=Column(String,unique=True,index=True)
     created_at=Column(DateTime,default=datetime.utcnow)