from datetime import datetime

from beanie import Document


class Users(Document):
    name: str
    password: str
    email: str
    created_at: datetime = datetime.now()
    deleted_at: datetime = None

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "name": "abc",
                "password": "abc"
            }
        }
