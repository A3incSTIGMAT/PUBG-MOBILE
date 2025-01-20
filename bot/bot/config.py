import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен Telegram-бота
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # URL вебхука
PORT = int(os.getenv("PORT", 8080))  # Порт для сервера
