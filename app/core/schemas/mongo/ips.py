from pydantic import BaseModel


class IPIn(BaseModel):
    ip: str
    ports: str
