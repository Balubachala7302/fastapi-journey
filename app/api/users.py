from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.schemas import UserCreate, UserOut
from app.core.permissions import require_role
from app.services.user_service import register_user
from app.core.response import success_response
from app.db.schemas import AdminDashboardResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -------------------------
# Register User
# -------------------------
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Creates a new user account with default role 'user'.",
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Registers a new user.

    - Validates input
    - Hashes password
    - Stores user in database
    """

    created_user = register_user(db, user)

    return success_response(
        data={
            "id": created_user.id,
            "email": created_user.email,
            "role": created_user.role
        },
        message="User registered successfully"
    )


# -------------------------
# Admin Dashboard
# -------------------------
@router.get(
    "/admin/dashboard",
    response_model=AdminDashboardResponse,
    summary="Admin Dashboard",
    description="Accessible only to users with admin role."
)
def admin_dashboard(
    current_user = Depends(require_role("admin"))
):
    return success_response(
        data={
            "email": current_user.email,
            "role": current_user.role
        },
        message="Welcome Admin"
    )