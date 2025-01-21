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

# Настройка вебхука
WEBHOOK_PATH = f"/webhook"
WEBHOOK_URL = f"https://<твой-домен>{WEBHOOK_PATH}"

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

# Обработчик сообщений (эхо-бот)
@router.message()
async def echo(message: Message):
    await message.answer(message.text)

# Регистрация маршрутов
dp.include_router(router)

# Функция для настройки вебхука
async def on_start(request: web.Request):
    return web.Response(text="Бот запущен и работает!")

# Веб-сервер с aiohttp
async def on_webhook(request: web.Request):
    update_data = await request.json()
    try:
        update = Update.parse_obj(update_data)
        await dp.process_update(update)  # Обрабатываем обновление через диспетчер
        return web.Response(status=200)
    except Exception as e:
        logger.error(f"Ошибка обработки обновления вебхука: {e}")
        return web.Response(status=400)

# Функция для регистрации вебхука
async def on_startup(app: web.Application):
    try:
        await bot.set_webhook(WEBHOOK_URL)
        logger.info(f"Вебхук установлен по адресу {WEBHOOK_URL}")
    except Exception as e:
        logger.error(f"Ошибка при установке вебхука: {e}")




 

















