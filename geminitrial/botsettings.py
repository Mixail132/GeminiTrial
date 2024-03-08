import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(token)
