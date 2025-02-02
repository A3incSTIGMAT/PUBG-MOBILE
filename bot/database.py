import aiosqlite

DB_NAME = "game.db"

async def get_player_stats(user_id: int) -> dict:
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute('SELECT rank, level FROM players WHERE user_id = ?', (user_id,))
        result = await cursor.fetchone()
        return {"rank": result[0], "level": result[1]} if result else {}
