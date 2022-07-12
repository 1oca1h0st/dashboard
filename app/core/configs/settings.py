from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@localhost/fastapi?charset=utf8"
    TEST_ENV: str

    class Config:
        env_file = ".env"


settings = Settings()


@lru_cache()
def get_settings():
    return Settings()
