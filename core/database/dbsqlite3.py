from datetime import datetime
import sqlite3
from typing import Any
async def check_user(id_user: int) -> bool:
    with sqlite3.connect('business_bot.db') as db:
        cursor = db.cursor()
        value = (id_user,) #Создание кортежа из 1 элемента
        cursor.execute(f"SELECT * FROM Users WHERE id_user = ?", value) #Value должно быть кортежем
        return bool(cursor.fetchone()) #Если есть зпись - True, если None - False
async def write_user(id_user: int, first_name: str, last_name: str, username: str, date_joined: datetime) -> None:
    if not await check_user(id_user): #Если нет такого пользователя
        with sqlite3.connect('business_bot.db') as db:
            value = (id_user, first_name, last_name, username, date_joined)
            cursor = db.cursor()
            cursor.execute("""
            INSERT INTO Users (id_user, first_name, last_name, username, date_joined)
            VALUES (?, ?, ?, ?, ?)
            """, value)

async def check_ban(id_user: int) -> bool: # Проверка на бан
    if await check_user(id_user): # Если подльзователь есть в бд => проверка на бан
        with sqlite3.connect('business_bot.db') as db:
            cursor = db.cursor()
            cursor.execute("""
                            SELECT banned FROM Users WHERE id_user = ?
                            """, (id_user,)) # Запрос на проверку поля banned для user
            return bool(cursor.fetchone()[0]) # возвращение кортежа (0,) если нет бана, или (1,) если бан, и переопределение в bool
    return False #Если пользователя нет в бд => False (отсутствие бана)


async def delete_user(id_user: int):
    if await check_user(id_user):
        with sqlite3.connect('business_bot.db') as db:
            cursor = db.cursor()
            cursor.execute("""SELECT * FROM Users WHERE id_user = ?""", (id_user,))
            deleted_user = cursor.fetchone()
            cursor.execute("""DELETE FROM Users WHERE id_user = ?""", (id_user,))
            return deleted_user
    return False

async def get_user(id_user: int) -> tuple:
    with sqlite3.connect('business_bot.db') as db:
        cursor = db.cursor()
        value = (id_user,) #Создание кортежа из 1 элемента
        cursor.execute(f"SELECT * FROM Users WHERE id_user = ?", value)
        return cursor.fetchone()

async def update_one_parametr_user(id_user: int, values: tuple): #Обновляет в таблице Users одно значение.
    if await check_user(id_user): # Если подльзователь есть в бд => проверка на бан
        with sqlite3.connect('business_bot.db') as db:
            cursor = db.cursor()
            #values содержит название изменяемого поля и его новое значение: ("banned", True)
            column_name, new_value = values
            cursor.execute(f"""UPDATE Users SET {column_name} = ? WHERE id_user = ?""", (new_value, id_user))
            cursor.execute("""SELECT * FROM Users WHERE id_user = ?""", (id_user,))
            updated_user = cursor.fetchone()
            return updated_user
    return False