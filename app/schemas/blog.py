from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    content: str
    tags: Optional[str] = None


class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str]= None
    content: Optional[str]= None
    tags: Optional[str]= None

class BlogOut(BlogBase):
    id: int
    author:str   
    class Config:
        from_attributes  = True
