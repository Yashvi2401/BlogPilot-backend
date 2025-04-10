from pydantic import BaseModel
from typing import Optional

class LoginBase(BaseModel):
    email: str
    password: str

class Login(LoginBase):
    pass

class LoginOut(LoginBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
