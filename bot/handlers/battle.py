from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.database import Database

router = Router()
db = Database()

@router.message(Command("battle"))
async def cmd_battle(message: Message):
    user = await db.fetch_one("SELECT * FROM players WHERE user_id = ?", (message.from_user.id,))
    if not user:
        await message.answer("❌ Сначала зарегистрируйтесь через /start")
        return
    
    await message.answer("⚔️ Вы в бою! Используйте:\n/attack - Атака\n/defend - Защита")
