from aiogram.types import Message
from aiogram.filters import CommandObject
from core.database.dbsqlite3 import delete_user, update_one_parametr_user
from core.utils.refactor import refac_user
async def del_user(message: Message, command: CommandObject):
    # Отправка аргументов через пробел после команды /del, к примеру, /del 12
    if not command.args.isdigit():
        message.answer("Введите id пользователя")
        return
    if command.args: #Если аргументов нет -> None
        result = await delete_user(int(command.args)) # Если пользователя с таким id нет -> None, иначе -> кортеж (строка из бд)
        if result: #Если кортеж
            user = await refac_user(*result)
            await message.answer(f"Удален: \nuser_id={user.user_id}"
                                 f"\nfirst_name={user.first_name}"
                                 f"\nlast_name={user.last_name}"
                                 f"\nusername={user.username}"
                                 f"\ndate_joined={user.data_joined}"
                                 f"\nbanned={user.banned}")
            return
        await message.answer("Пользователь с таким id не найден")

async def ban_user(message: Message, command: CommandObject):
    if not command.args.isdigit():
        message.answer("Введите id пользователя")
        return
    if command.args:  # Если аргументов нет -> None
        values = ("banned", True)
        result = await update_one_parametr_user(int(command.args), values)  # Если пользователя с таким id нет -> None, иначе -> кортеж (строка из бд)
        if result:  # Если кортеж
            user = await refac_user(*result)
            await message.answer(f"Забанен: \nuser_id={user.user_id}"
                                 f"\nfirst_name={user.first_name}"
                                 f"\nlast_name={user.last_name}"
                                 f"\nusername={user.username}"
                                 f"\ndate_joined={user.data_joined}"
                                 f"\nbanned={user.banned}")
            return
        await message.answer("Пользователь с таким id не найден")

async def unban_user(message: Message, command: CommandObject):
    if not command.args.isdigit():
        message.answer("Введите id пользователя")
        return
    if command.args:  # Если аргументов нет -> None
        values = ("banned", False)
        result = await update_one_parametr_user(int(command.args), values)  # Если пользователя с таким id нет -> None, иначе -> кортеж (строка из бд)
        if result:  # Если кортеж
            user = await refac_user(*result)
            await message.answer(f"Разбанен: \nuser_id={user.user_id}"
                                 f"\nfirst_name={user.first_name}"
                                 f"\nlast_name={user.last_name}"
                                 f"\nusername={user.username}"
                                 f"\ndate_joined={user.data_joined}"
                                 f"\nbanned={user.banned}")
            return
        await message.answer("Пользователь с таким id не найден")
