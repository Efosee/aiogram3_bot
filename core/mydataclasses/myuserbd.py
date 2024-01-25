from dataclasses import dataclass
from datetime import datetime
@dataclass
class MyUserBD:
    user_id: int
    first_name: str | None
    last_name: str | None
    username: str | None
    data_joined: datetime | None
    banned: bool | None