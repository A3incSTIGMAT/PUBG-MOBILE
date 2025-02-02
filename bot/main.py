import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiohttp import web
from bot.config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH
from bot.handlers import base, battle, shop, admin

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Подключение всех роутеров
dp.include_routers(
    base.router,
    battle.router,
    shop.router,
    admin.router
)

# Вебхук-обработчик
async def on_webhook(request: web.Request):
    try:
        data = await request.json()
        update = Update(**data)
        await dp.feed_update(bot, update)
        return web.Response(status=200)
    except Exception as e:
        return web.Response(status=500)

# Настройка вебхука
async def setup_webhook(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)

# Запуск приложения
def run_app():
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, on_webhook)
    app.on_startup.append(setup_webhook)
    web.run_app(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

if __name__ == "__main__":
    run_app()










    





 

















