#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "12217554"))
API_HASH = environ.get("API_HASH", "3f0f161f48f440f87266f397c656e521")
BOT_TOKEN = environ.get("BOT_TOKEN""7793632205:AAFDz03a8y0u7rzMPSD8QUkCqIn90fdspno")

OWNER = int(environ.get("OWNER", "769398389"))
CREDIT = environ.get("CREDIT", "mad848506_bot")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")



AUTH_USER = os.environ.get('AUTH_USERS', '769398389').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))








