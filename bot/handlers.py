from aiogram import Router, F
from aiogram.types import Message

router = Router()  # Инициализируем роутер

# Обработчик команды /start
@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик всех остальных сообщений
@router.message()
async def echo_message(message: Message):
    await message.answer(f"Вы отправили: {message.text}")
