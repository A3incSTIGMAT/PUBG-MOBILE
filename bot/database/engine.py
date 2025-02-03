# bot/database/engine.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def create_async_engine(db_url: str):
    """Создает асинхронный движок для работы с БД."""
    return create_async_engine(db_url, echo=True)

async def get_session(engine) -> AsyncSession:
    """Возвращает асинхронную сессию для работы с БД."""
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
