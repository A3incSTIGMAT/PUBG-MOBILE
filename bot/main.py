import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.enums import ParseMode
from aiohttp import web
from bot.config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH
from bot.handlers.base import router as base_router
from bot.handlers.battle import router as battle_router
from bot.handlers.shop import router as shop_router
from bot.handlers.admin import router as admin_router

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Проверка наличия обязательных переменных
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен в переменных окружения!")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Подключение всех обработчиков
dp.include_router(base_router)
dp.include_router(battle_router)
dp.include_router(shop_router)
dp.include_router(admin_router)

async def on_webhook(request: web.Request):
    """Обработчик входящих вебхуков"""
    try:
        data = await request.json()
        update = Update.model_validate(data, context={"bot": bot})
        await dp.feed_update(bot, update)
        return web.Response(status=200)
    except Exception as e:
        logger.error(f"Ошибка обработки обновления: {str(e)}", exc_info=True)
        return web.Response(status=500)

async def setup_webhook(app: web.Application):
    """Настройка вебхука при запуске приложения"""
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)
    logger.info(f"Вебхук успешно установлен: {WEBHOOK_URL}")

def run_app():
    """Запуск приложения"""
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, on_webhook)
    app.on_startup.append(setup_webhook)
    
    port = int(os.environ.get("PORT", 10000))
    web.run_app(
        app,
        host="0.0.0.0",
        port=port,
        access_log=logging.getLogger("aiohttp.access")
    )

if __name__ == "__main__":
    logger.info("Запуск бота в режиме вебхука")
    run_app()










    





 

















