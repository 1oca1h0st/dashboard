from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@localhost/fastapi?charset=utf8"


settings = Settings()
