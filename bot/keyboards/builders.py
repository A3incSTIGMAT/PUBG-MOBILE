from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚔️ Бой", callback_data="battle")
    builder.button(text="🛒 Магазин", callback_data="shop")
    builder.button(text="📊 Профиль", callback_data="profile")
    builder.adjust(2)
    return builder.as_markup()
