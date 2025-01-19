from aiogram import Bot, Dispatcher
from bot.handlers import start  # Импортируем обработчики

BOT_TOKEN = "ВашТокен"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)

if __name__ == "__main__":
    print("Бот успешно запущен!")

