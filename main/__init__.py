from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int("11321821")
API_HASH = "bbf63cf902c2548c31963ccd88c4c6f7"
BOT_TOKEN = "5664270366:AAEpERaV7G45boA7pw3oFnZ9Te83pfWLvDA"
BOT_UN = "ret_ddbot"

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
