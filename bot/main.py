from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env файла
load_dotenv()

# Загружаем токен и URL вебхука
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT", 8000)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)

# Создаем диспетчер с аргументом bot
dp = Dispatcher(bot=bot)

# Функция для обработки старта приложения
async def on_startup(app):
    # Устанавливаем webhook
    await bot.set_webhook(WEBHOOK_URL)

# Обработчик для получения webhook-запросов
async def webhook(request):
    json_str = await request.json()  # Получаем данные запроса
    update = Update(**json_str)  # Преобразуем их в объект Update
    await dp.process_update(update)  # Обрабатываем обновление
    return web.Response(status=200)  # Ответ

# Создаем приложение aiohttp и добавляем обработчик webhook
app = web.Application(on_startup=[on_startup])
app.router.add_post('/webhook', webhook)

# Запуск приложения
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=int(PORT))  # Запускаем сервер

 сервер



