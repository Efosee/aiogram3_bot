from aiogram.filters import BaseFilter
from aiogram.types import Message
from core.utils.config import config

class isAdmin(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id in config.ADMINS_IDS