"""
view module for create massages to user
"""
import server_controller


def get_connection_status():
    return server_controller.get_connection_status()


def add_id(sender_name, msg_text):
    if server_controller.set_id(msg_text):
        return "OK. Enter year of birth please."
    return "Invalid input. Enter ID number please."


def start_message():
    server_controller.set_start_message()
    return "hey! \n what your id? "


def add_birth_year(sender_name, msg_text):
    if server_controller.set_year(msg_text):
        return "Very good. Choose a care specialty."
    return "Invalid input. Enter year of birth."


def add_type_of_doctors(sender_name, msg_text):
    if server_controller.add_specialty(msg_text):
        return "Excellent. Now we'll be looking for an appointment for the next two weeks."
    return "Invalid input. Choose care specialty please."


def all_is_fill(sender_name, msg_text):
    return "We will now look for a meeting for the next two weeks and will be updated soon."

# def get_msg():
#     sender_name = " "
#     msg_text = input()
#     switcher = {
#         1: add_id,
#         2: add_birth_year,
#         3: add_type_of_doctors,
#         4: all_is_fill
#     }
#     rep_str = switcher.get(get_connection_status(), "I do not understand you.")(sender_name, msg_text)
#     print(rep_str)
#
# start_message()
# while get_connection_status() != 4:
#     get_msg()

