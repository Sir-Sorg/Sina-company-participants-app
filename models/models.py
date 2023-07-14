from pydantic import BaseModel


class User(BaseModel):
    username_or_email: str
    password: str


class Viwer(BaseModel):
    username: str
    db_id: str
