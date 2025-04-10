from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import hashing
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.routers.authentication import user_login

router = APIRouter(
    tags=['User'],
    prefix='/user'
)

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await db.execute(select(User).where(User.email == user.email))
    if existing_user.scalars().first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hashing.Hash.bcrypt(user.password)
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    user_login(User.email,User.password)
    
    return new_user
@router.get("/{email}",response_model=UserOut)
async def show_user(email:str,db: AsyncSession= Depends(get_db)):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user