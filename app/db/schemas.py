from pydantic import BaseModel, EmailStr, ConfigDict


# =========================
# USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)


# =========================
# POST SCHEMAS
# =========================

class PostCreate(BaseModel):
    title: str
    content: str


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# TOKEN SCHEMAS
# =========================

class TokenResponse(BaseModel):
    access_token: str
    token_type: str