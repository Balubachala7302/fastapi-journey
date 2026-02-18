from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.schemas import UserCreate, UserOut
from app.core.permissions import require_role
from app.services.user_service import register_user
from app.core.response import success_response


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -------------------------
# Register User
# -------------------------
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

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
@router.get("/admin/dashboard")
def admin_dashboard(
    current_user=Depends(require_role("admin"))
):
    return success_response(
        data={
            "email": current_user.email,
            "role": current_user.role
        },
        message="Welcome Admin"
    )