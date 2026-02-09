from fastapi import HTTPException, status

class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class NotFoundException(AppException):
    def __init__(self, detail="Resource not found"):
        super().__init__(status.HTTP_404_NOT_FOUND, detail)


class UnauthorizedException(AppException):
    def __init__(self, detail="Unauthorized"):
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail)