from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@localhost/fastapi?charset=utf8"
    MONGO_DATABASE_URI = "mongodb://root:1QAZ2wsx@localhost/?retryWrites=true&w=majority"
    TEST_ENV: str

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
