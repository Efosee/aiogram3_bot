import sqlite3

# Создание базы данных Users
db = sqlite3.connect(r'D:\Programming\Python projects\telegram bot\business_bot\business_bot.db')
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id_user INTEGER PRIMARY KEY,
first_name VARCHAR,
last_name VARCHAR,
username VARCHAR,
date_joined DATETIME,
banned BOOLEAN DEFAULT False
)
""")
# Выполнение запроса
db.commit()
# Закрытие подлючения
db.close()



# Создание базы данных Products
db = sqlite3.connect(r'D:\Programming\Python projects\telegram bot\business_bot\business_bot.db')
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
id_product INTEGER PRIMARY KEY,
title VARCHAR,
price_per_month INTEGER
)
""")
# Выполнение запроса
db.commit()
# Закрытие подлючения
db.close()


#Создание базы данных Purchases
db = sqlite3.connect(r'D:\Programming\Python projects\telegram bot\business_bot\business_bot.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Purchases (
        id_user INTEGER,
        id_product INTEGER,
        months_purchased INTEGER,
        price INTEGER,
        activation_date DATE,
        expiration_date DATE,
        PRIMARY KEY (id_user, id_product),
        FOREIGN KEY (id_user) REFERENCES Users(id_user),
        FOREIGN KEY (id_product) REFERENCES Products(id_product)
    )
''')
# Выполнение запроса
db.commit()
# Закрытие подлючения
db.close()