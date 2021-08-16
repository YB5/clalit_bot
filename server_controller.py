from datetime import date
import data_server
import automation_fill


def get_connection_status():
    return data_server.r_get("connection_status").connection_status


def set_connection_status(status):
    if status == data_server._r_server("connection_status") + 1:
        data_server.r_set("connection_status", status)


def set_id(new_id):
    if new_id.isnumeric():
        data_server.r_set("ID", new_id)
        set_connection_status(data_server.r_get("ID_FILL"))
        return True
    return False


def get_id():
    return data_server.r_get("ID")


def set_year(year):
    if year.isnumeric() and int(year) > 1901 and int(year) < date.today().year:
        data_server.r_set("BirthYear", year)
        set_connection_status(data_server.r_get("BIRTHYEAR_FILL"))
        return True
    return False


def get_year(year):
    return data_server.r_get("BirthYear")


def set_start_message():
    set_connection_status(data_server.r_get("START_MESSAGE"))


def find_appointment():
    # todo date check
    return automation_fill.run_web(data_server.r_get("ID"), data_server.r_get("BirthYear"), data_server.r_get("Specialty"))


def add_specialty(msg_text):
    specialty = ["orthopedics", "otolaryngology", "breast surgeon", "women", "skin", "eyes"]
    if any([msg_text == x for x in specialty]):
        data_server.r_set("Specialty", msg_text)
        set_connection_status(data_server.r_get("SPECIALTY_FILL"))
        return True
    return False


data_server.init()
