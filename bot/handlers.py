from aiogram import Router, F
from aiogram.types import Message

router = Router()  # Инициализируем роутер

# Обработчик команды /start
@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@router.message(F.text == "/help")
async def help_command(message: Message):
    commands = (
        "/start - Начать игру или взаимодействие с ботом\n"
        "/help - Список всех команд\n"
        "/rules - Правила игры\n"
        "/about - О боте\n"
        "/battle - Вызвать игрока на PvP\n"
        "/accept - Принять вызов\n"
        "/attack - Атаковать соперника\n"
        "/defend - Защититься от атаки\n"
        "/exit - Выйти из текущей игры\n"
        "/profile - Ваш профиль\n"
        "/stats - Статистика игрока\n"
        "/leaderboard - Таблица лидеров\n"
        "/health - Узнать текущее здоровье\n"
        "/shop - Открыть магазин\n"
        "/buy - Купить предмет\n"
        "/sell - Продать предмет\n"
        "/inventory - Ваш инвентарь\n"
        "/equip - Экипировать предмет\n"
        "/unequip - Снять предмет\n"
        "/balance - Проверить баланс\n"
        "/daily - Получить ежедневный бонус\n"
        "/upgrade - Улучшить оружие или броню\n"
        "/addcoins - Добавить монеты (только для админов)\n"
        "/resetstats - Сбросить статистику игрока"
    )
    await message.answer(commands)

# Обработчик команды /rules
@router.message(F.text == "/rules")
async def rules_command(message: Message):
    rules = (
        "1. Пройдите обучение.\n"
        "2. Сражайтесь с другими игроками.\n"
        "3. Участвуйте в PvP сражениях.\n"
        "4. Собирайте предметы и улучшайте свое оружие.\n"
        "5. Побеждайте врагов и достигайте новых уровней."
    )
    await message.answer(rules)

# Обработчик команды /about
@router.message(F.text == "/about")
async def about_command(message: Message):
    await message.answer("Этот бот позволяет вам сражаться с другими игроками и улучшать ваше оружие. Сражайтесь, получайте награды и становитесь лучшим!")

# Обработчик команды /battle
@router.message(F.text == "/battle")
async def battle_command(message: Message):
    await message.answer("Вызывайте другого игрока на бой, используя команду /accept")

# Обработчик команды /accept
@router.message(F.text == "/accept")
async def accept_command(message: Message):
    await message.answer("Вы приняли вызов на бой! Ждите ответа.")

# Обработчик команды /attack
@router.message(F.text == "/attack")
async def attack_command(message: Message):
    await message.answer("Вы атаковали соперника!")

# Обработчик команды /defend
@router.message(F.text == "/defend")
async def defend_command(message: Message):
    await message.answer("Вы защищаетесь от атаки!")

# Обработчик команды /exit
@router.message(F.text == "/exit")
async def exit_command(message: Message):
    await message.answer("Вы вышли из игры.")

# Обработчик команды /profile
@router.message(F.text == "/profile")
async def profile_command(message: Message):
    await message.answer("Вот ваш профиль.")

# Обработчик команды /stats
@router.message(F.text == "/stats")
async def stats_command(message: Message):
    await message.answer("Вот ваша статистика.")

# Обработчик команды /leaderboard
@router.message(F.text == "/leaderboard")
async def leaderboard_command(message: Message):
    await message.answer("Вот таблица лидеров.")

# Обработчик команды /health
@router.message(F.text == "/health")
async def health_command(message: Message):
    await message.answer("Вот ваше текущее здоровье.")

# Обработчик команды /shop
@router.message(F.text == "/shop")
async def shop_command(message: Message):
    await message.answer("Открылся магазин! Что хотите купить?")

# Обработчик команды /buy
@router.message(F.text == "/buy")
async def buy_command(message: Message):
    await message.answer("Вы купили предмет!")

# Обработчик команды /sell
@router.message(F.text == "/sell")
async def sell_command(message: Message):
    await message.answer("Вы продали предмет!")

# Обработчик команды /inventory
@router.message(F.text == "/inventory")
async def inventory_command(message: Message):
    await message.answer("Вот ваш инвентарь.")

# Обработчик команды /equip
@router.message(F.text == "/equip")
async def equip_command(message: Message):
    await message.answer("Вы экипировали предмет!")

# Обработчик команды /unequip
@router.message(F.text == "/unequip")
async def unequip_command(message: Message):
    await message.answer("Вы сняли предмет!")

# Обработчик команды /balance
@router.message(F.text == "/balance")
async def balance_command(message: Message):
    await message.answer("Вот ваш баланс.")

# Обработчик команды /daily
@router.message(F.text == "/daily")
async def daily_command(message: Message):
    await message.answer("Вы получили свой ежедневный бонус!")

# Обработчик команды /upgrade
@router.message(F.text == "/upgrade")
async def upgrade_command(message: Message):
    await message.answer("Вы улучшили ваше оружие или броню!")

# Обработчик команды /addcoins (только для админов)
@router.message(F.text == "/addcoins")
async def addcoins_command(message: Message):
    # Можно добавить проверку на роль админа
    await message.answer("Монеты добавлены.")

# Обработчик команды /resetstats (только для админов)
@router.message(F.text == "/resetstats")
async def resetstats_command(message: Message):
    # Можно добавить проверку на роль админа
    await message.answer("Статистика игрока сброшена.")

