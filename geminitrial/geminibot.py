# This a trial bot called 'checker' that uses Gemini to answer any questions
# It sends the requests to the server where Gemini is working
# And gets the responses from the server
import time
import requests
from botsettings import bot


@bot.message_handler(commands=['start'])
def start(message):
    uid = message.chat.id
    username = message.from_user.first_name
    bot.send_message(uid, f"Hey!, {username} , you can ask what you're interested in")


@bot.message_handler(content_types=['text'])
def text(message):
    """
    Gets the text question from a user.
    Redirects it to the third party server.
    Gemini working there receives the question.
    After processing, it generates the answer.
    The answer then is returned to the user.
    :param message: a Telegram user text message
    :return: None
    """
    uid = message.chat.id
    url = "http://mixail132.pythonanywhere.com"
    question = message.text
    data = {"question": question}
    answer = requests.post(url=url, json=data)
    answer = answer.json()
    bot.send_message(uid, answer['answer'])


bot.infinity_polling(
    none_stop=True,
    timeout=60,
    long_polling_timeout=60,
    allowed_updates=['message']
)
time.sleep(3)
