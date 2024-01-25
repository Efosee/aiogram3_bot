import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from core.utils.config import config
from core.handlers.users.handlerstart import first_start, restart
from core.handlers.admins.userupdate import del_user, ban_user, unban_user
from core.filters.authentication import AuthenticationFilter
from core.filters.isadmin import isAdmin
from core.middlewaries.verification import AccessVerificationMiddleware
async def main():
    dp = Dispatcher()
    bot = Bot(token=config.TOKEN)

    dp.message.middleware.register(AccessVerificationMiddleware()) #Проверка на бан пользователя
    dp.message.register(first_start, CommandStart(), ~AuthenticationFilter()) #При первом запуске
    dp.message.register(restart, CommandStart(), AuthenticationFilter()) #При повторном запуске (пользователь есть в бД)


    dp.message.register(del_user, Command("del"), isAdmin())
    dp.message.register(ban_user, Command("ban"), isAdmin())
    dp.message.register(unban_user, Command("unban"), isAdmin())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

#TODO реализовать user handler для обработки "Каталог" и "Профиль"