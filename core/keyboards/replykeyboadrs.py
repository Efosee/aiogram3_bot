from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text="⚜️Каталог"),
        KeyboardButton(text="💼Профиль")],
        [KeyboardButton(text="🛒История покупок")
    ]], resize_keyboard=True)