import os
from dotenv import load_dotenv

load_dotenv()

ROOT_ID: int = int(os.getenv("ROOT_ID", "959489052"))  # Обязательно задать ROOT_ID в переменных окружения

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "8814517159:AAHsBxK8iVOw6kbNHa12uUTA7Oj2hLyfzno")    # Обязательно задать BOT_TOKEN в переменных окружения

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Добавьте его в переменные окружения.")

if ROOT_ID == 0:
    raise RuntimeError("ROOT_ID не задан! Добавьте его в переменные окружения.")

DB_PATH: str = os.getenv("DB_PATH", "data/bot.db")

TIMEZONE: str = "Europe/Moscow"
