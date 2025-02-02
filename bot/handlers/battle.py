from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("battle"))
async def cmd_battle(message: Message):
    await message.answer("⚔️ Вы в режиме боя! Выберите противника:")
