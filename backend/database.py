from sqlalchemy.ext.asyncio import create_async_engine 
from sqlmodel.ext.asyncio.session import AsyncSession
from config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL, 
    echo=True,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

async def get_session():
    async with AsyncSession(engine) as session:
        yield session