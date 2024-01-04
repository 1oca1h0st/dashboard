from bson import ObjectId
from pydantic import BaseModel, Field

from core.models.mongo.id import PyObjectId


class DemoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = None
    description: str = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
