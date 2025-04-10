from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app import hashing
from app.db.session import get_db
from app.models.user import User
from app.schemas.authentication import Token
from app.jwtTokens import create_access_token

router = APIRouter(
    tags=["Authentication"],
)

@router.post('/login', response_model=Token)
async def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == form_data.username))
    db_user = result.scalars().first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Invalid email")

    if not hashing.Hash.verify(form_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
