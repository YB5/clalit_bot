"""
interacting with the Telegram API and create a Flask server setup.

"""
from flask import Flask, Response, request
import requests as requests
import view_server


app = Flask(__name__)


# Telegram API
TOKEN = '1943783961:AAEZlvH1DPwdw4yrCxM6XgDMImlsHHhQGOQ'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=' \
                            'https://7159b331a7fc.ngrok.io/message'.format(TOKEN)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/')
def sanity():
    """
    sanity check for the flask server
    :return: str message
    """
    return "Server is running"


@app.route('/message', methods=["POST"])
def handle_message():
    """
    Every message sent in a bot activates this function.

    From the json file, extract the message, sender name, and chat id.
    Interpret the message.
    Send a reply message via telegram api.

    :return: Response. status of the reply message
    """
    resp = request.get_json()
    if resp.get("message", "") == "":
        return Response("success")
    msg_text = resp["message"]["text"]
    sender_name = resp["message"]["from"]["first_name"]
    chat_id = resp["message"]["chat"]["id"]
    rep_str = view_server.interpret_message(sender_name, msg_text)
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, chat_id, str(rep_str)))
    if res.status_code == 200:
        return Response("success")
    return Response("fail")


if __name__ == '__main__':
    app.run(port=5002,debug=True)

#
# import telebot
# API_KEY = "1919382703:AAErQuc42X-pjIW7OrR3a3CsHc0Yd-s-ybk"
#
# bot = telebot.TeleBot(API_KEY)
#
# @bot.message_handler(commands=['Start'])
# def greet(message):
#     bot.reply_to(message,"hey! ")
#
# @bot.message_handler(commands=['shalom'])
# def hllow(message):
#     bot.reply_to(message,"jjjjj!")
#
# bot.polling()