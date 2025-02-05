# bot/middlewares/throttling.py
from aiogram import Dispatcher
from aiogram.types import Message
import time

class ThrottlingMiddleware:
    def __init__(self, limit=1.0):
        self.limit = limit
        self.last_time = {}

    async def __call__(self, handler, event: Message, data: dict):
        user_id = event.from_user.id
        current_time = time.time()

        if user_id in self.last_time:
            if current_time - self.last_time[user_id] < self.limit:
                await event.answer("🚫 Подождите перед следующим запросом!")
                return

        self.last_time[user_id] = current_time
        return await handler(event, data)
