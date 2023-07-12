from pydantic import BaseModel


class Twitter(BaseModel):
    name: str
    id: str
