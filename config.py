from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 5))

DATABASE = os.getenv("DATABASE", "luxury.db")