#TODO создать функцию, которая переделает кортеж из бд в словарь, а затем распокует его в класс MyUserDB
from datetime import datetime
from core.mydataclasses.myuserbd import MyUserBD
async def refac_user(user_id: int, first_name: str, last_name: str, username: str, date_joined: datetime, banned: bool) -> MyUserBD:
    date_joined = datetime.strptime(date_joined, "%Y-%m-%d %H-%M-%S")
    banned = True if banned else False
    return MyUserBD(user_id=user_id, first_name=first_name, last_name=last_name, username=username, data_joined=date_joined, banned=banned)