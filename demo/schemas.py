from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username:str
    email:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None

class DisplayUser(BaseModel):
    username:str
    email:str
    class Config:
        orm_mode=True



