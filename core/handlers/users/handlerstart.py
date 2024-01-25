from aiogram.types import Message
from datetime import timedelta
from core.database.dbsqlite3 import write_user
from core.keyboards.replykeyboadrs import main_keyboard


# (message.date + timedelta(hours=3)).strftime("%Y-%m-%d %H-%M-%S") -> получаем время UTC и прибавляем 3 часа => время МСК
async def first_start(message: Message): # /start для первого запуска
    await message.answer("Привет, сейчас запишу тебя в свой блокнот!", reply_markup=main_keyboard)
    await write_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                     message.from_user.username, (message.date + timedelta(hours=3)).strftime("%Y-%m-%d %H-%M-%S"))

async def restart(message: Message): # /start Если бот ранее был запущен
    await message.answer("Ты уже зарегистрирован!", reply_markup=main_keyboard)
