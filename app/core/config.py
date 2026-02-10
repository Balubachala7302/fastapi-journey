from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME:str="FastAPI Journey"
    DEBUG:bool=False

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

@lru_cache
def get_settings():
    return Settings()