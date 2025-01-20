from aiogram import Router, F
from aiogram.types import Message

router = Router()

# Обработчик команды /start
@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@router.message(F.text == "/help")
async def help_command(message: Message):
    commands = (
        "/start - Начать игру или взаимодействие с ботом\n"
        "/help - Список всех команд\n"
        "/rules - Правила игры\n"
        "/about - О боте\n"
        "/battle - Вызвать игрока на PvP\n"
        "/accept - Принять вызов\n"
        "/attack - Атаковать соперника\n"
        "/defend - Защититься от атаки\n"
        "/exit - Выйти из текущей игры\n"
        "/profile - Ваш профиль\n"
        "/stats - Статистика игрока\n"
        "/leaderboard - Таблица лидеров\n"
        "/health - Узнать текущее здоровье\n"
        "/shop - Открыть магазин\n"
        "/buy - Купить предмет\n"
        "/sell - Продать предмет\n"
        "/inventory - Ваш инвентарь\n"
        "/equip - Экипировать предмет\n"
        "/unequip - Снять предмет\n"
        "/balance - Проверить баланс\n"
        "/daily - Получить ежедневный бонус\n"
        "/upgrade - Улучшить оружие или броню\n"
        "/addcoins - Добавить монеты (только для админов)\n"
        "/resetstats - Сбросить статистику игрока"
    )
    await message.answer(commands)



