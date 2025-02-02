import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, Update
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен вашего бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

# Порт для Render
port = int(os.getenv("PORT", 10000))

# Путь и URL вебхука
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://pubg-mobile-zzmw.onrender.com{WEBHOOK_PATH}"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()  # ✅ Исправлено: без передачи бота
router = Router()
dp.include_router(router)

# Обработчики команд
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

@router.message(Command("help"))
async def cmd_help(message: Message):
    commands = (
        "/start - Начать взаимодействие с ботом\n"
        "/help - Список команд\n"
        "/rules - Правила\n"
        "/about - О боте"
    )
    await message.answer(commands)

# ... остальные обработчики (аналогично)

# Обработчик вебхука
async def on_webhook(request: web.Request):
    try:
        data = await request.json()
        update = Update(**data)
        await dp.feed_update(bot, update)  # ✅ Передаем бота здесь
        return web.Response(status=200)
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return web.Response(status=500)

# Настройка вебхука
async def setup_webhook(app):
    await bot.set_webhook(WEBHOOK_URL)
    logger.info(f"Webhook установлен: {WEBHOOK_URL}")

# Запуск сервера
def run_app():
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, on_webhook)
    app.on_startup.append(setup_webhook)
    logger.info(f"Запуск бота на порту {port}")
    web.run_app(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    run_app()











    





 

















