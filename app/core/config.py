from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Any, Dict, Optional
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool
    API_V1_PREFIX: str

    # Database
    DATABASE_TYPE: str
    DATABASE_URL: Optional[str] = None
    DATABASE_CONNECT_ARGS: Dict[str, Any] = {}
    ENVIRONMENT: str   # log setting

    @property
    def sqlalchemy_database_url(self) -> str:
        if self.DATABASE_TYPE == "sqlite":
            return self.DATABASE_URL or "sqlite:///./sql_app.db"
        elif self.DATABASE_TYPE == "postgresql":
            if not self.DATABASE_URL:
                raise ValueError("DATABASE_URL must be set for PostgreSQL")
            return self.DATABASE_URL
        else:
            raise ValueError(f"Unsupported database type: {self.DATABASE_TYPE}")

    @property
    def database_connect_args(self) -> Dict[str, Any]:
        if self.DATABASE_TYPE == "sqlite":
            return {"check_same_thread": False}
        return {}

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
