from beanie import PydanticObjectId
from fastapi import APIRouter

from core.models.mongo.users import Users
from core.schemas.mongo.users import UserOut

router = APIRouter()


@router.post("/create")
async def create(user: Users):
    user = await user.create()
    return user


@router.get("/{uid}", response_model=UserOut)
async def get_user_by_id(uid: PydanticObjectId):
    user = await Users.get(uid)
    return user
