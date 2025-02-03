from sqlalchemy.ext.asyncio import AsyncSession

class DatabaseManager:
    """Класс для работы с базой данных."""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_player(self, user_id: int):
        # Ваша реализация методов...
