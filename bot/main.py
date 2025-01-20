from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env файла
load_dotenv()

# Загружаем токен и URL вебхука
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT", 8000)

# Отладочный код для проверки переменных окружения
if not BOT_TOKEN or not WEBHOOK_URL:
    raise ValueError("BOT_TOKEN или WEBHOOK_URL не указаны. Проверьте файл .env")
else:
    print(f"BOT_TOKEN: {BOT_TOKEN}, WEBHOOK_URL: {WEBHOOK_URL}")

# Инициализация бота
bot = Bot(token=BOT_TOKEN)

# Создаем диспетчер с аргументом bot
dp = Dispatcher()

# Функция для обработки старта приложения
async def on_startup(app):
    # Устанавливаем webhook
    await bot.set_webhook(WEBHOOK_URL)

# Обработчик для команды /start
@dp.message()
async def send_welcome(message: types.Message):
    if message.text.startswith('/start'):
        await message.reply("Привет! Я твой бот. Чем могу помочь?")

# Обработчик для получения webhook-запросов
async def webhook(request):
    json_str = await request.json()  # Получаем данные запроса
    update = Update(**json_str)  # Преобразуем их в объект Update
    await dp.process_update(update)  # Обрабатываем обновление
    return web.Response(status=200)  # Ответ

# Создаем приложение aiohttp
app = web.Application()

# Добавляем обработчик старта в список on_startup
app.on_startup.append(on_startup)

# Добавляем обработчик для webhook
app.router.add_post('/webhook', webhook)

# Запуск приложения
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=int(PORT))  # Запускаем сервер










