from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("buy"))
async def start_buy(message: Message, state: FSMContext):
    await message.answer("📝 Введите название предмета:")
    await state.set_state("waiting_item_name")

# Исправленная строка:
@router.message(F.text, F.state == "waiting_item_name")  # ✅
async def process_buy(message: Message, state: FSMContext):
    item_name = message.text.strip()
    # ... логика покупки ...
    await state.clear()

