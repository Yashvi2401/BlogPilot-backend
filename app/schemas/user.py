from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes  = True