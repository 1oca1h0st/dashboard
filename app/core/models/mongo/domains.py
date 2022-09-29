from beanie import Document


class Domain(Document):
    domain: str

    class Settings:
        name = "domains"

    class Config:
        schema_extra = {
            "example": {
                "domain": "example.com"
            }
        }
