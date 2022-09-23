from beanie import PydanticObjectId
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from core.controllers.users import UsersController
from core.models.mongo.users import Users
from core.schemas.mongo.users import UserOut

router = APIRouter()


@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    auth = UsersController()
    access_token = await auth.authenticate_user(form_data.username, form_data.password)
    return access_token


@router.post("/create")
async def create(user: Users):
    user = await user.create()
    return user


@router.get("/{uid}", response_model=UserOut)
async def get_user_by_id(uid: PydanticObjectId):
    user = await Users.get(uid)
    return user
