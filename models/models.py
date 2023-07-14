from pydantic import BaseModel


class User(BaseModel):
    username_or_email: str
    password: str
