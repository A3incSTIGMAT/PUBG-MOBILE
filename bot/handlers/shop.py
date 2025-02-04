from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
import sqlite3

router = Router()

# Команда /shop
@router.message(Command("shop"))
async def show_shop(message: Message):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price FROM items')
    items = cursor.fetchall()
    conn.close()
    
    if not items:
        await message.answer("🛒 Магазин пуст!")
        return
    
    shop_list = "🛒 Доступные товары:\n"
    for item in items:
        shop_list += f"- {item[0]} ({item[1]} coins)\n"
    
    await message.answer(shop_list)

# Команда /buy
@router.message(Command("buy"))
async def start_buy(message: Message, state: FSMContext):
    await message.answer("Введите название предмета:")
    await state.set_state("waiting_item_name")

@router.message(F.text, state="waiting_item_name")
async def process_buy(message: Message, state: FSMContext):
    item_name = message.text.strip()
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    # Проверяем существование предмета
    cursor.execute('SELECT item_id, price FROM items WHERE name = ?', (item_name,))
    item = cursor.fetchone()
    
    if not item:
        await message.answer("❌ Такого предмета нет в магазине!")
        await state.clear()
        return
    
    # Проверяем баланс игрока
    cursor.execute('SELECT balance FROM players WHERE user_id = ?', (message.from_user.id,))
    balance = cursor.fetchone()[0]
    
    if balance < item[1]:
        await message.answer("⛔ Недостаточно средств!")
        await state.clear()
        return
    
    # Обновляем баланс и добавляем предмет в инвентарь
    cursor.execute('UPDATE players SET balance = balance - ? WHERE user_id = ?', (item[1], message.from_user.id))
    cursor.execute('INSERT INTO inventory (user_id, item_id) VALUES (?, ?)', (message.from_user.id, item[0]))
    conn.commit()
    conn.close()
    
    await message.answer(f"✅ Вы купили {item_name}!")
    await state.clear()  # проверь правильность кода

