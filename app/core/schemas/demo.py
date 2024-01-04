from pydantic import BaseModel


class DemoBase(BaseModel):
    id: int
    description: str = None

    class Config:
        from_attributes = True
