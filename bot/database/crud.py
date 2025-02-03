from sqlalchemy.ext.asyncio import AsyncSession
from .models import Player

class DatabaseManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_player(self, user_id: int) -> Player:
        result = await self.session.execute(
            select(Player).where(Player.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def create_player(self, user_id: int, username: str):
        new_player = Player(user_id=user_id, username=username)
        self.session.add(new_player)
        await self.session.commit()
