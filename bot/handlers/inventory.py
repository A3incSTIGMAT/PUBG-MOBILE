from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import sqlite3

router = Router()

# Команда /inventory
@router.message(Command("inventory"))
async def show_inventory(message: Message):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT i.name, inv.quantity, inv.equipped 
        FROM inventory inv
        JOIN items i ON inv.item_id = i.item_id
        WHERE inv.user_id = ?
    ''', (message.from_user.id,))
    
    items = cursor.fetchall()
    conn.close()
    
    if not items:
        await message.answer("🎒 Ваш инвентарь пуст!")
        return
    
    inventory_list = "🎒 Инвентарь:\n"
    for item in items:
        status = " (экипировано)" if item[2] else ""
        inventory_list += f"- {item[0]} x{item[1]}{status}\n"
    
    await message.answer(inventory_list)

# Команда /equip
@router.message(Command("equip"))
async def start_equip(message: Message, state: FSMContext):
    await message.answer("Введите название предмета для экипировки:")
    await state.set_state("waiting_equip_item")

@router.message(F.text, state="waiting_equip_item")
async def process_equip(message: Message, state: FSMContext):
    item_name = message.text.strip()
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE inventory 
        SET equipped = CASE 
            WHEN item_id = (SELECT item_id FROM items WHERE name = ?) THEN TRUE
            ELSE FALSE
        END
        WHERE user_id = ?
    ''', (item_name, message.from_user.id))
    
    conn.commit()
    conn.close()
    await message.answer(f"🛡️ Вы экипировали {item_name}!")
    await state.clear()
