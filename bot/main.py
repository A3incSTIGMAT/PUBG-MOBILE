import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiohttp import web
from bot.config import config
from bot.database import create_async_engine, get_session
from bot.handlers import base, battle, shop
from bot.middlewares import ThrottlingMiddleware
from bot.models import Base
from bot.utils import handle_exception
from bot.database import DatabaseManager
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.filters import StateFilter

# Определите свои состояния FSM
class MyState(StatesGroup):
    waiting_item_name = State()

# Используйте фильтр StateFilter
@router.message(StateFilter(MyState.waiting_item_name), F.text)
async def handler(message: Message):
    # Логика обработчика
    pass

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def on_startup():
    """
    Инициализация БД и настройка вебхуков при старте.
    """
    # Инициализация БД (с использованием Alembic миграций, если нужно)
    try:
        engine = create_async_engine(config.DB_URL)
        async with engine.begin() as conn:
            # Здесь можно использовать Alembic для миграций, если они настроены.
            # await conn.run_sync(Base.metadata.create_all)  # Комментарий для использования Alembic
            pass  # Убедитесь, что миграции выполняются с Alembic

        # Настройка вебхука
        await bot.set_webhook(config.WEBHOOK_URL)
        logger.info(f"Вебхук установлен на {config.WEBHOOK_URL}")

    except Exception as e:
        logger.error(f"Ошибка при старте: {e}", exc_info=True)
        raise

def setup_middlewares(dp: Dispatcher):
    """
    Настройка миддлварей для диспетчера.
    """
    dp.update.middleware(ThrottlingMiddleware())  # Поставить ограничение на количество запросов

def setup_routers(dp: Dispatcher):
    """
    Настройка маршрутов для бота.
    """
    dp.include_routers(
        base.router,
        battle.router,
        shop.router
    )

async def webhook_handler(request: web.Request):
    """
    Обработчик вебхука для получения обновлений от Telegram.
    """
    try:
        update = await request.json()
        await dp.feed_update(bot, update)
        return web.Response(text="OK")
    except Exception as e:
        handle_exception(e)  # Используем вспомогательную функцию для обработки ошибок
        return web.Response(status=500)

def handle_exception(e: Exception):
    """
    Функция для централизованной обработки исключений.
    """
    logger.error(f"Произошла ошибка: {str(e)}", exc_info=True)

if __name__ == "__main__":
    """
    Основной запуск приложения.
    """
    try:
        config.validate()  # Валидация конфигурации
        bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
        dp = Dispatcher()

        setup_middlewares(dp)
        setup_routers(dp)

        app = web.Application()
        app.router.add_post(config.WEBHOOK_PATH, webhook_handler)

        # Запуск приложения с учетом переменной окружения PORT
        web.run_app(
            app,
            host="0.0.0.0",
            port=int(os.getenv("PORT", 8000))
        )

    except Exception as e:
        logger.error(f"Ошибка при запуске приложения: {e}", exc_info=True)
        exit(1)











    





 

















