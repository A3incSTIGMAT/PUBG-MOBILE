from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from dotenv import load_dotenv
import os
import logging

# Загружаем переменные окружения из .env файла
load_dotenv()

# Загружаем токен и URL вебхука
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT", 8000)

# Проверка наличия BOT_TOKEN и WEBHOOK_URL
if not BOT_TOKEN or not WEBHOOK_URL:
    raise ValueError("BOT_TOKEN или WEBHOOK_URL не указаны в .env файле.")

# Инициализация бота
bot = Bot(token=BOT_TOKEN)

# Создаем диспетчер с аргументом bot
dp = Dispatcher(bot=bot)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для обработки старта приложения
async def on_startup(app):
    # Устанавливаем webhook
    logger.info(f"Setting webhook with URL: {WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)

# Обработчик для получения webhook-запросов
async def webhook(request):
    try:
        json_str = await request.json()  # Получаем данные запроса
        update = Update(**json_str)  # Преобразуем их в объект Update
        await dp.process_update(update)  # Обрабатываем обновление

        logger.info(f"Webhook received: {json_str}")  # Логирование принятого запроса
        return web.Response(status=200)  # Ответ
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return web.Response(status=500)  # Ответ в случае ошибки

# Создаем приложение aiohttp
app = web.Application()

# Добавляем обработчик старта в список on_startup
app.on_startup.append(on_startup)

# Добавляем обработчик для webhook
app.router.add_post('/webhook', webhook)

# Запуск приложения
if __name__ == '__main__':
    logger.info(f"Starting server on port {PORT}...")
    web.run_app(app, host='0.0.0.0', port=int(PORT))  # Запускаем сервер








