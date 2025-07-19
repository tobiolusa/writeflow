from pydantic import BaseModel 

class BlogBase(BaseModel):
    title: str
    content : str
    author : str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    author: str | None = None

class BlogResponse(BlogBase):
    id: int

class Config:
        orm_mode = True