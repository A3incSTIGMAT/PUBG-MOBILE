import os
from bot.config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID",895844198))
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    WEBHOOK_PATH = "/webhook"
    DB_FILE = "game.db"

    @classmethod
    def check_env(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN не установлен в .env!")
