# bot/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

class DatabaseManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    # Методы для работы с базой данных...

# Если это функция для получения сессии
def get_session() -> AsyncSession:
    engine = create_async_engine('sqlite+aiomysql://localhost/testdb')
    SessionLocal = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )
    return SessionLocal()
