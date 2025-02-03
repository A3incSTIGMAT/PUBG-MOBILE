from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.database import DatabaseManager
from bot.keyboards.builders import main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, db: DatabaseManager):
    player = await db.get_player(message.from_user.id)
    if not player:
        await db.create_player(
            user_id=message.from_user.id,
            username=message.from_user.username
        )
    await message.answer(
        "🎮 Добро пожаловать в бот!",
        reply_markup=main_menu()
    )
