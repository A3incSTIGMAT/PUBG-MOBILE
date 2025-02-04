from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.database import DatabaseManager, get_session

router = Router()

@router.message(Command("battle"))
async def cmd_battle(message: Message):
    async with get_session() as session:
        db = DatabaseManager(session)  # ✅ Сессия передана
        # Ваша логика боя...
