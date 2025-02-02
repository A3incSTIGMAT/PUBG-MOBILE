from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@router.message(Command("help"))
async def help_command(message: Message):
    commands = (
        "📜 Список доступных команд:\n\n"
        "/start - Начать игру или взаимодействие\n"
        "/help - Показать это сообщение\n"
        "/rules - Правила игры\n"
        "/about - Информация о боте\n"
        "/battle - Вызвать игрока на PvP\n"
        "/accept - Принять вызов\n"
        "/attack - Атаковать соперника\n"
        "/defend - Защититься от атаки\n"
        "/exit - Выйти из текущей игры\n"
        "/profile - Ваш профиль\n"
        "/stats - Статистика игрока\n"
        "/leaderboard - Таблица лидеров\n"
        "/health - Текущее здоровье\n"
        "/shop - Открыть магазин\n"
        "/buy - Купить предмет\n"
        "/sell - Продать предмет\n"
        "/inventory - Ваш инвентарь\n"
        "/equip - Экипировать предмет\n"
        "/unequip - Снять предмет\n"
        "/balance - Проверить баланс\n"
        "/daily - Ежедневный бонус\n"
        "/upgrade - Улучшить снаряжение\n"
        "/addcoins - Добавить монеты (админ)\n"
        "/resetstats - Сбросить статистику"
    )
    await message.answer(commands)



