import aiosqlite
from config import Config

class Database:
    def __init__(self):
        self.db_name = Config.DB_FILE

    async def execute(self, query: str, params: tuple = ()):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(query, params)
            await db.commit()

    async def fetch_one(self, query: str, params: tuple = ()):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute(query, params)
            return await cursor.fetchone()

    async def init_db(self):
        await self.execute('''
            CREATE TABLE IF NOT EXISTS players (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                balance INTEGER DEFAULT 100,
                health INTEGER DEFAULT 100
            )
        ''')
