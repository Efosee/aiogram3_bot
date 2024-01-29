from aiogram.client import bot
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram import Bot
from core.keyboards.inlinekeyboards import paginator, Pagination
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InputMediaPhoto

#TODO переделать в json и продумать синхронизацию в sqlite с целью онлайн добавления/редактирования товаров из админ панели
products = {0:[200, "media/example1.png"],
            1:[400, "media/example2.png"],
            2:[600, "media/example3.png"]}
async def get_catalog(message: Message, bot: Bot):
    photo = FSInputFile("media/example1.png")
    await bot.send_photo(message.from_user.id, photo=photo, reply_markup= await paginator(200))

async def get_product(call: CallbackQuery, callback_data: Pagination):
    page_num = callback_data.page
    page = page_num + 1 if page_num < 2 else 0
    if callback_data.action == "prev":
        page= page_num - 1 if page_num > 0 else 2
    price = int(products[int(page)][0])
    url_picture = str(products[int(page)][1])
    photo = FSInputFile(url_picture)
    media = InputMediaPhoto(media=photo)
    await call.message.edit_media(media=media, reply_markup=await paginator(price, page))