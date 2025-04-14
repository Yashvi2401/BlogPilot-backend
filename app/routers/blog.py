from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from dependencies import get_current_user
from gemini import generate_summary
from models.blog import Blog
from models.user import User
from schemas.blog import BlogCreate, BlogOut
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)


@router.post("/", response_model=BlogOut)
async def create_blog(blog: BlogCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_blog = Blog(
        title=blog.title,
        content=blog.content,
        user_id=current_user.id,
        author=current_user.username,
        tags=blog.tags
    )
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog


@router.get("/", response_model=Page[BlogOut])
async def get_blogs(db: AsyncSession = Depends(get_db)):
    return await paginate(db, select(Blog))

add_pagination(router)

@router.get("/{id}",response_model=Page[BlogOut])
async def show_blog(id:int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Blog).where(Blog.id == id))
    blog = result.scalars().first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog
    



@router.put("/{id}")
async def update_blog(id: int, updated_blog: BlogCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Blog).where(Blog.id == id))
    blog = result.scalars().first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="You can only edit your own blogs")

    blog.title = updated_blog.title
    blog.content = updated_blog.content
    blog.updated_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(blog)
    return blog


@router.delete("/{id}")
async def delete_blog(id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Blog).where(Blog.id == id))
    blog = result.scalars().first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="You can only delete your own blogs")

    await db.delete(blog)
    await db.commit()
    return {"message": "Blog deleted successfully"}


@router.get("/{search_string}", response_model=list[BlogOut])
async def search_blog_by_tag(search_string: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Blog).where(Blog.tags.ilike(f"%{search_string}%") | Blog.author.ilike(search_string) | Blog.content.ilike(f"%{search_string}%")))
    return result.scalars().all()


@router.get("/{id}/summary")
async def get_blog_summary(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Blog).where(Blog.id == id))
    blog = result.scalars().first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    summary = await generate_summary(blog.content)
    return {"summary": summary}
