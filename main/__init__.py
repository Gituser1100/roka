from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=11321821, cast=int)
API_HASH = config("API_HASH", default=bbf63cf902c2548c31963ccd88c4c6f7)
BOT_TOKEN = config("BOT_TOKEN", default=5664270366:AAEpERaV7G45boA7pw3oFnZ9Te83pfWLvDA)
BOT_UN = config("BOT_UN", default=ret_ddbot)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
