import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Основные настройки
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    ADMIN_IDS: list = list(map(int, os.getenv("ADMIN_IDS", "").split(',')))
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")
    WEBHOOK_PATH: str = os.getenv("WEBHOOK_PATH", "/webhook")
    
    # Настройки БД
    DB_URL: str = os.getenv("DB_URL", "sqlite+aiosqlite:///game.db")
    
    # Проверка конфигурации
    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN не задан в .env!")
        
        if not cls.WEBHOOK_URL:
            raise ValueError("WEBHOOK_URL не задан!")

config = Settings()
        
