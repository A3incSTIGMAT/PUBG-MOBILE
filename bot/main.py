import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiohttp import web
from bot.config import config
from bot.database import create_async_engine, get_session
from bot.handlers import base, battle, shop

async def on_startup():
    # Инициализация БД
    engine = create_async_engine(config.DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Настройка вебхука
    await bot.set_webhook(config.WEBHOOK_URL)

def setup_middlewares(dp: Dispatcher):
    dp.update.middleware(ThrottlingMiddleware())

def setup_routers(dp: Dispatcher):
    dp.include_routers(
        base.router,
        battle.router,
        shop.router
    )

async def webhook_handler(request: web.Request):
    try:
        update = await request.json()
        await dp.feed_update(bot, update)
        return web.Response(text="OK")
    except Exception as e:
        logging.error(f"Ошибка: {e}", exc_info=True)
        return web.Response(status=500)

if __name__ == "__main__":
    config.validate()
    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    
    setup_middlewares(dp)
    setup_routers(dp)
    
    app = web.Application()
    app.router.add_post(config.WEBHOOK_PATH, webhook_handler)
    
    web.run_app(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000))
    )










    





 

















