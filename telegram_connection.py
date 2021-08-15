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
                            'http://990394205607.ngrok.io/message'.format(TOKEN)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/sanity')
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
    switcher = {
        0: view_server.start_message(),
        1: view_server.add_id(sender_name, msg_text),
        2: view_server.add_birth_year(sender_name, msg_text),
        3: view_server.add_type_of_doctors(sender_name, msg_text),
        4: view_server.all_is_fill(sender_name, msg_text)
    }
    rep_str = switcher.get(view_server.get_connection_status(), "I do not understand you.")
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, chat_id, rep_str))
    if res.status_code == 200:
        return Response("success")
    return Response("fail")


if __name__ == '__main__':
    app.run(port=9002)