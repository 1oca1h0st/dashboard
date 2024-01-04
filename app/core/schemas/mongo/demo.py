from bson import ObjectId
from pydantic import BaseModel, Field

from core.models.mongo.id import PyObjectId


class DemoBase(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        # 支持别名，使用alias进行配置
        populate_by_name = True
        # 支持嵌套python class类型
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
