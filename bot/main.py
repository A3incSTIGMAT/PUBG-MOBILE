import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, Update
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен. Укажите его в переменных окружения.")

# Порт для Render
port = int(os.getenv("PORT", 10000))

# Путь и URL вебхука
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://pubg-mobile-zzmw.onrender.com{WEBHOOK_PATH}"

# Инициализация бота, роутера и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
router = Router()
dp = Dispatcher()
dp.include_router(router)  # Подключаем роутер к диспетчеру

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@router.message(Command("help"))
async def cmd_help(message: Message):
    commands = (
        "/start - Начать взаимодействие с ботом\n"
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
        "3. Используйте команды для взаимодействия."
    )
    await message.answer(rules)

# Обработчик команды /about
@router.message(Command("about"))
async def cmd_about(message: Message):
    about_info = (
        "Я бот, созданный для демонстрации возможностей aiogram 3.x.\n"
        "Использую вебхуки и работаю на Render!"
    )
    await message.answer(about_info)

# Эхо-обработчик
@router.message()
async
from shop_handlers import router as shop_router
from inventory_handlers import router as inventory_router

dp.include_router(shop_router)
dp.include_router(inventory_router)










    





 

















