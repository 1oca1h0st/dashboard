from pydantic import BaseModel


class DomainIn(BaseModel):
    domain: str
