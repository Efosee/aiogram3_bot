from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import CallbackData, InlineKeyboardBuilder


class Pagination(CallbackData, prefix="pag"):
    action: str | None = None
    page: int | None = None


async def paginator(costs: int, page: int=0):
    builder = InlineKeyboardBuilder()

    builder.button(text="⬅️", callback_data=Pagination(action="prev", page=page).pack())
    builder.button(text=f"{costs} руб.", callback_data="costs") # Инлайн кнопки должны иметь хотя бы одно опциональное поле: callback_data, url, switch_inline_query и т.д.
    builder.button(text="➡️", callback_data=Pagination(action="next", page=page).pack())
    builder.button(text="Купить", callback_data=str(costs))
    builder.adjust(3,1)
    return builder.as_markup()


