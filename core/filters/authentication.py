from aiogram.filters import BaseFilter
from aiogram.types import Message
from core.database.dbsqlite3 import check_user

# Фильтр на проверку занесен (зарегистрирован) ли пользователь в бд
class AuthenticationFilter(BaseFilter):
    async def __call__(self, message: Message):
        return await check_user(message.from_user.id)