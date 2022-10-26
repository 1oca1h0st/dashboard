from datetime import timedelta, datetime

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from starlette import status

from core.configs.settings import settings
from core.models.mongo.users import Users


class UsersController:
    def __init__(
            self,
            SECRET_KEY=settings.SECRET_KEY,
            ALGORITHM=settings.ALGORITHM,
            ACCESS_TOKEN_EXPIRE_MINUTES=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    ):
        self.SECRET_KEY = SECRET_KEY
        self.ALGORITHM = ALGORITHM
        self.ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encode_jwt

    # 验证用户名密码
    # TODO 后续增加验证码逻辑
    async def authenticate_user(self, username: str, password: str):
        user = await Users.find_one(Users.name == username)
        if user is not None:
            if self.verify_password(password, user.password):
                access_token = self.create_access_token(
                    data={"sub": user.name}, expires_delta=timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
                )
                return {"access_token": access_token, "token_type": "bearer"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"}
        )


if __name__ == '__main__':
    users = UsersController()
    print(users.authenticate_user("1", "2"))
