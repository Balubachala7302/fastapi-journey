from fastapi import HTTPException, status, Request
from app.core.redis import redis_client

RATE_LIMIT = 5
WINDOW_SECONDS = 60


async def rate_limiter(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    current = redis_client.get(key)

    if current is None:
        redis_client.setex(key, WINDOW_SECONDS, 1)
        return

    if int(current) >= RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Try again later."
        )

    redis_client.incr(key)