import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Config:
    TOKEN: str
    ADMINS_IDS: list[int]
def get_config() -> Config:
    return Config(TOKEN=os.environ.get("BOT_TOKEN"),
                  ADMINS_IDS=list(map(int,os.environ.get("ADMINS_IDS").split(","))))

config = get_config()