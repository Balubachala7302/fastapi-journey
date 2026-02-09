from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME:str="FastAPI Journey"
    ENV:str="dev"

    SECRET_KEY: str
    ALGORITHM: str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()