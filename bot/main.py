import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, Update
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен вашего бота, полученный через BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set. Please set it as an environment variable.")

# Получение порта из переменной окружения для Render
port = int(os.getenv("PORT", 10000))  # Порт по умолчанию - 10000

# Динамический путь вебхука
WEBHOOK_PATH = f"/webhook"  # Простой путь для вебхука, без токена в URL
WEBHOOK_URL = f"https://pubg-mobile-zzmw.onrender.com{WEBHOOK_PATH}"  # Указываем домен и путь

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Создание маршрутизатора
router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@router.message(Command("help"))
async def cmd_help(message: Message):
    commands = (
        "/start - Начать игру или взаимодействие с ботом\n"
        "/help - Список всех команд\n"
        "/rules - Правила игры\n"
        "/about - О боте"
    )
    await message.answer(commands)

# Обработчик команды /rules
@router.message(Command("rules"))
async def cmd_rules(message: Message):
    rules = (
        "1. Будьте вежливы с ботом.\n"
        "2. Не отправляйте спам.\n"
        "3. Следите за тем, чтобы ваши запросы были понятными.\n"
        "4. Используйте команды для взаимодействия с ботом."
    )
    await message.answer(rules)

# Обработчик команды /about
@router.message(Command("about"))
async def cmd_about(message: Message):
    about_info = (
        "Я бот, созданный для демонстрации работы с библиотекой aiogram.\n"
        "Я могу обрабатывать команды, отвечать на сообщения и помогать вам!"
    )
    await message.answer(about_info)

# Обработчик сообщений (эхо-бот)
@router.message()
async def echo(message: Message):
    await message.answer(message.text)

# Регистрация маршрутов
dp.include_router(router)

# Функция для настройки вебхука







    





 

















