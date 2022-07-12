from pydantic import BaseModel, validator


class DemoRequests(BaseModel):
    t_id: int

    @validator("t_id")
    def check_t_id(cls, v):
        if v > 10 or v < 3:
            raise ValueError('t_id must be less than 10 and greater than 3')
        return v
