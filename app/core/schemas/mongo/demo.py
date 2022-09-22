from bson import ObjectId
from pydantic import BaseModel, Field

from core.schemas.mongo.id import PyObjectId


class DemoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
