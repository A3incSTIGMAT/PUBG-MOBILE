from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware
import time

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=0.5):
        self.last_update = {}
        self.limit = limit
        super().__init__()

    async def on_pre_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        current_time = time.time()
        
        if user_id in self.last_update:
            if current_time - self.last_update[user_id] < self.limit:
                await message.answer("⚠️ Слишком много запросов!")
                raise CancelHandler()
        
        self.last_update[user_id] = current_time
