from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any
from core.database.dbsqlite3 import check_ban
from core.utils.config import config

# Проверка доступа (бан пользователя)
class AccessVerificationMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:
        if not await check_ban(event.from_user.id): # Если пользователь не забанен
            return await handler(event, data)


