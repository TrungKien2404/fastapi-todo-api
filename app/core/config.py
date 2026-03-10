from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "FastAPI Todo API"
    DEBUG: bool = True
    SECRET_KEY: str = "secret123"

settings = Settings()