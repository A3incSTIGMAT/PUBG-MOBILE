from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from bot.database import get_player_stats

router = Router()

@router.message(Command("battle"))
async def cmd_battle(message: Message):
    await message.answer("⚔️ Выберите противника из списка:")

@router.message(Command("profile"))
async def cmd_profile(message: Message):
    stats = await get_player_stats(message.from_user.id)
    await message.answer(
        f"👤 <b>Профиль:</b>\n"
        f"Ранг: {stats['rank']}\n"
        f"Уровень: {stats['level']}",
        parse_mode="HTML"
    )
