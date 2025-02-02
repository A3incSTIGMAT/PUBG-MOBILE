import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
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

# Инициализация бота
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)  # Создаём диспетчер с переданным ботом

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    commands = (
        "/start - Начать игру или взаимодействие с ботом\n"
        "/help - Список всех команд\n"
        "/rules - Правила игры\n"
        "/about - О боте"
    )
    await message.answer(commands)

# Обработчик команды /rules
@dp.message(Command("rules"))
async def cmd_rules(message: Message):
    rules = (
        "1. Будьте вежливы с ботом.\n"
        "2. Не отправляйте спам.\n"
        "3. Следите за тем, чтобы ваши запросы были понятными.\n"
        "4. Используйте команды для взаимодействия с ботом."
    )
    await message.answer(rules)

# Обработчик команды /about
@dp.message(Command("about"))
async def cmd_about(message: Message):
    about_info = (
        "Я бот, созданный для демонстрации работы с библиотекой aiogram.\n"
        "Я могу обрабатывать команды, отвечать на сообщения и помогать вам!"
    )
    await message.answer(about_info)

# Обработчик сообщений (эхо-бот)
@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

# Функция для обработки вебхуков
async def on_webhook(request: web.Request):
    try:
        data = await request.json()
        update = Update(**data)
        await dp.process_update(update)
        return web.Response(status=200)
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        return web.Response(status=500)

# Функция для настройки вебхука
async def setup_webhook(app):
    # Устанавливаем вебхук
    await bot.set_webhook(WEBHOOK_URL)
    logger.info(f"Webhook set to: {WEBHOOK_URL}")

# Функция для запуска aiohttp-сервера
def run_app():
    app = web.Application()

    # Регистрируем обработчик для вебхука
    app.router.add_post(WEBHOOK_PATH, on_webhook)

    # Устанавливаем вебхук для бота
    app.on_startup.append(setup_webhook)

    # Запускаем сервер на указанном порту
    logger.info(f"Starting bot on port {port}")
    web.run_app(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    run_app()











    





 

















