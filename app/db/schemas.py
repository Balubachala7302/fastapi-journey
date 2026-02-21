from pydantic import BaseModel, EmailStr, ConfigDict


# =========================
# AUTH SCHEMAS
# =========================

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "strongpassword123"
            }
        }
    )


class TokenData(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    message: str
    data: TokenData

    model_config = ConfigDict(from_attributes=True)


# =========================
# USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "strongpassword123"
            }
        }
    )


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)


class UserProfileData(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)


class UserProfileResponse(BaseModel):
    message: str
    data: UserProfileData

    model_config = ConfigDict(from_attributes=True)


# =========================
# POST SCHEMAS
# =========================

class PostCreate(BaseModel):
    title: str
    content: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "My First Post",
                "content": "This is my first FastAPI post."
            }
        }
    )


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class PostResponse(BaseModel):
    message: str
    data: PostOut

    model_config = ConfigDict(from_attributes=True)


# =========================
# ADMIN SCHEMAS
# =========================

class AdminDashboardData(BaseModel):
    email: str
    role: str

    model_config = ConfigDict(from_attributes=True)


class AdminDashboardResponse(BaseModel):
    message: str
    data: AdminDashboardData

    model_config = ConfigDict(from_attributes=True)


# =========================
# GENERIC RESPONSE
# =========================

class MessageResponse(BaseModel):
    message: str

    model_config = ConfigDict(from_attributes=True)