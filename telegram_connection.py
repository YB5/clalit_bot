# """
# interacting with the Telegram API and create a Flask server setup.
#
# """
import telebot
import automation_fill
import view_server
API_KEY = "1919382703:AAErQuc42X-pjIW7OrR3a3CsHc0Yd-s-ybk"

bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "hey! \n what your id? ")


@bot.message_handler(content_types=['text'])
def msg_handler(pm):
    sender_name = " "
    msg_text = pm.text
    switcher = {
            1: view_server.add_id,
            2: view_server.add_birth_year,
            3: view_server.add_type_of_doctors,
            4: view_server.all_is_fill
    }
    connection_status = view_server.get_connection_status()
    if connection_status == 0:
        rep_str = view_server.start_message()
    else:
        rep_str = switcher.get(connection_status, "I do not understand you.")(sender_name, msg_text)
    sent_msg = bot.send_message(pm.chat.id, rep_str)
    #bot.send_message(pm.chat.id, sent_msg)
    #bot.register_next_step_handler(sent_msg, name_handler)  # Next message will call the name_handler function


# def name_handler(pm):
#     id = pm.text
#
#     sent_msg = bot.send_message(pm.chat.id, view_server.add_id(id))
#
#     bot.register_next_step_handler(sent_msg, age_handler, id)  # Next message will call the age_handler function
#
#
# def age_handler(pm, id):
#     year = pm.text
#     bot.send_message(pm.chat.id, f"Your name is {id}, and your age is {year}.")
#     #automation_fill.run_web(id,year)




bot.polling()