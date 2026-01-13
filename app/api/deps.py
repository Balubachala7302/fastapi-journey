from app.db.database import get_db
from app.core.security import get_current_user
from fastapi import Depends

def get_current_active_user(
    user = Depends(get_current_user)
):
    return user