from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from typing import Callable, Awaitable, Dict, Any
from core.database.dbsqlite3 import check_ban
from core.utils.config import config

# Проверка доступа (бан пользователя)
class AccessVerificationMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        # В словаре data по ключу event_from_user хранится объект класса User с данными о пользователе
        if not await check_ban(data['event_from_user'].id): # Если пользователь не забанен
            return await handler(event, data)

