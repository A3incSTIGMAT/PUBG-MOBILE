import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-app.onrender.com/webhook")
WEBHOOK_PATH = "/webhook"
ADMIN_ID = int(os.getenv("ADMIN_ID", 895844198))  # Замените на ваш ID
