from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

from bot.config import BOT_TOKEN, WEBHOOK_URL, PORT
from bot.handlers import router

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Регистрация роутеров
dp.include_router(router)

# Обработчик входящих запросов
async def handle_webhook(request):
    update = await request.json()
    await bot.feed_update(update)
    return web.Response()

# Настройка веб-сервера
def main():
    app = web.Application()
    app.router.add_post("/", handle_webhook)

    # Устанавливаем вебхук
    async def on_startup():
        await bot.set_webhook(WEBHOOK_URL)

    async def on_shutdown():
        await bot.delete_webhook()
        await bot.session.close()

    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_shutdown)

    web.run_app(app, port=PORT)

if __name__ == "__main__":
    main()
