from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from models import Blog
import schemas

app = FastAPI()

# Create blog post
@app.post("/blogs", response_model=schemas.BlogResponse)
async def create_blog(blog: schemas.BlogCreate):
    blog_obj = await Blog.create(**blog.dict())
    return await schemas.BlogResponse.from_tortoise_orm(blog_obj)

# Get all blog posts
@app.get("/blogs", response_model=list[schemas.BlogResponse])
async def get_blogs():
    blogs = await Blog.all()
    return [await schemas.BlogResponse.from_tortoise_orm(blog) for blog in blogs]

# Get a single post by ID
@app.get("/blogs/{blog_id}", response_model=schemas.BlogResponse)
async def get_blog(blog_id: int):
    blog = await Blog.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return await schemas.BlogResponse.from_tortoise_orm(blog)

# Update a post
@app.put("/blogs/{blog_id}", response_model=schemas.BlogResponse)
async def update_blog(blog_id: int, blog_data: schemas.BlogUpdate):
    blog_obj = await Blog.get_or_none(id=blog_id)
    if not blog_obj:
        raise HTTPException(status_code=404, detail="Blog post not found")
    
    # Update only the fields provided in the request
    update_data = blog_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(blog_obj, field, value)

    await blog_obj.save()
    return await schemas.BlogResponse.from_tortoise_orm(blog_obj)

# Delete blog
@app.delete("/blogs/{blog_id}")
async def delete_blog(blog_id: int):
    blog = await Blog.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    await blog.delete()
    return {"message": "Blog post deleted successfully"}

# Register ORM
register_tortoise(
    app,
    db_url='sqlite://blog.db',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)