from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from models import Blog
import schemas

app = FastAPI()

@app.post("/blogs", response_model=schemas.BlogResponse)
async def create_blog(blog: schemas.BlogCreate):
    blog_obj = await Blog.create(**blog.dict())
    return await schemas.BlogResponse.from_tortoise_orm(blog_obj)

@app.get("/blogs", response_model=list[schemas.BlogResponse])
async def get_blogs():
    blogs = await Blog.all()
    return [await schemas.BlogResponse.from_tortoise_orm(blog) for blog in blogs]

@app.get("blogs/{blog_id}", response_model=schemas.BlogResponse)
async def get_blog(blog_id:int):
    blog = await Blog.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")