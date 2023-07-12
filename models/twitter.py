from pydantic import BaseModel


class Twitter(BaseModel):
    name: str
    password: str
    username: str
