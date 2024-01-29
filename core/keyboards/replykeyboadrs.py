from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text="⚜️Каталог"),
        KeyboardButton(text="🛍️Мои покупки")],
       [KeyboardButton(text="💼Профиль")],
       [KeyboardButton(text="🎧Связь с админитрацией")]],
    resize_keyboard=True)
