from pydantic import BaseModel, Field


class User(BaseModel):
    username_or_email: str = Field('JjooYadate2397')
    password: str = Field('ps4plus14')


class Viwer(BaseModel):
    username: str = Field('JjooYadate2397')
    db_id: str = Field('64b191fa90b8e5e94ae68d22')
