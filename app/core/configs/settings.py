from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@localhost/fastapi?charset=utf8"
    TEST_ENV: str

    MONGO_DB_HOST: str
    MONGO_DB_NAME: str
    MONGO_DB_USER: str
    MONGO_DB_PWD: str

    class Config:
        """
        使用 pydantic-dotenv 读取 .env 文件
        1. 变量大小写不敏感
        2. 不支持中文
        """
        env_file = ".env"


settings = Settings()


@lru_cache()
def get_settings():
    """
    使用lru_cache缓存settings内的内容，减少io重复读取带来的效率损失，提升性能
    """
    return Settings()
