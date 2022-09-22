from bson import ObjectId
from pydantic import BaseModel, Field

from core.models.mongo.id import PyObjectId


class UserOut(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        # 支持别名，使用alias进行配置
        allow_population_by_field_name = True
        # 支持嵌套python class类型
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
