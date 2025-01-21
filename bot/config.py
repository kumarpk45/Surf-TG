import os
from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "28836709"))
    API_HASH = getenv("API_HASH", "7141c6095cd69aa0278daa12faa0cbad")
    BOT_TOKEN = getenv("BOT_TOKEN", "7790882826:AAFztT-k0YF_u55C1fiDSUgvgr9vJXnDe60")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", " ")
    BASE_URL = getenv("BASE_URL", "https://thiraitg.koyeb.app/").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://moviebuzz203:nfyAaEZy4wUz6Dib@thiraiwebtg.h86nh.mongodb.net/?retryWrites=true&w=majority&appName=ThiraiWebTG")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002342014518").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "ThiraiTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "ThiraiTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
