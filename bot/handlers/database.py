import sqlite3

def init_db():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    # Таблица игроков
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            balance INTEGER DEFAULT 100,
            health INTEGER DEFAULT 100
        )
    ''')
    
    # Таблица предметов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            type TEXT  # weapon, armor, consumable
        )
    ''')
    
    # Таблица инвентаря
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            user_id INTEGER,
            item_id INTEGER,
            quantity INTEGER DEFAULT 1,
            equipped BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (user_id) REFERENCES players(user_id),
            FOREIGN KEY (item_id) REFERENCES items(item_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Инициализация БД при старте
init_db()
def populate_test_data():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    # Добавляем предметы
    cursor.executemany('''
        INSERT INTO items (name, price, type) 
        VALUES (?, ?, ?)
    ''', [
        ("Аптечка", 50, "consumable"),
        ("Броня 3 уровня", 200, "armor"),
        ("M416", 300, "weapon")
    ])
    
    conn.commit()
    conn.close()

# Вызовите эту функцию один раз при первом запуске
populate_test_data()
