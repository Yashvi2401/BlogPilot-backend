import asyncio
from db.session import async_engine
from models import blog, user
from db.base import Base


async def create_all():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(create_all())
