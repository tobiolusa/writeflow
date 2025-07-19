from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Blog

class BlogBase(BaseModel):
    title: str
    content: str
    author: str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    author: str | None = None

# Generate BlogResponse using pydantic_model_creator
BlogResponse = pydantic_model_creator(Blog, name="BlogResponse")