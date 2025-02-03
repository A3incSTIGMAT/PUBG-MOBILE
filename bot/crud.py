from sqlalchemy.ext.asyncio import AsyncSession

class DatabaseManager:
    """Класс для работы с базой данных."""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_player(self, user_id: int):
        # Пример реализации метода
        # Здесь может быть запрос к базе данных для получения информации о игроке
        result = await self.session.execute(
            "SELECT * FROM players WHERE user_id = :user_id", {"user_id": user_id}
        )
        player = result.fetchone()
        return player
