from datetime import date
import data_server


def get_connection_status():
    return data_server.connection_status


def set_connection_status(status):
    if status == data_server.connection_status + 1:
        data_server.connection_status = status


def set_id(new_id):
    if new_id.isnumeric():
        data_server.ID = new_id
        set_connection_status(data_server.ID_FILL)
        return True
    return False


def get_id():
    return data_server.ID


def set_year(year):
    if year.isnumeric() and int(year) > 1901 and int(year) < date.today().year:
        data_server.BirthYear = year
        set_connection_status(data_server.BIRTHYEAR_FILL)
        return True
    return False


def get_year(year):
    return data_server.BirthYear


def set_start_message():
    set_connection_status(data_server.START_MESSAGE)


def add_specialty(msg_text):
    specialty = ["orthopedics", "otolaryngology", "women"]
    if any([msg_text == x for x in specialty]):
        data_server.Specialty = msg_text
        set_connection_status(data_server.SPECIALTY_FILL)
        return True
    return False
