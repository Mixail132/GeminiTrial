import os
import time
import telebot
from views import gemini_ai
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    uid = message.chat.id
    username = message.from_user.first_name
    bot.send_message(uid, f"Hey!, {username} , you can ask what you're interested in")


@bot.message_handler(content_types=['text'])
def text(message):
    uid=message.chat.id
    question = message.text
    answer = gemini_ai(question)
    bot.send_message(uid, answer)


bot.infinity_polling(
    none_stop=True,
    timeout=60,
    long_polling_timeout=60,
    allowed_updates=['message']
)
time.sleep(3)
