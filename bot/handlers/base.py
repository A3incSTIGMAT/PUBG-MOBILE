from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("🎮 Добро пожаловать в PUBG Mobile Бот!\nИспользуй /help")

@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "📜 <b>Основные команды:</b>\n"
        "/start - Начать игру\n"
        "/help - Справка\n"
        "/profile - Профиль\n"
        "/shop - Магазин\n"
        "/inventory - Инвентарь"
    )
    await message.answer(help_text, parse_mode="HTML")
