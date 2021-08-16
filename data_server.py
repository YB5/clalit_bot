# ID = 0
# BirthYear = 1900
# Specialty = ""
# START_MESSAGE = 1
# ID_FILL = 2
# BIRTHYEAR_FILL = 3
# SPECIALTY_FILL = 4
# connection_status = 0
"""
redis db connection & actions
"""
import redis

_r_server = redis.Redis(
    host='localhost',
    port='6379')


def r_set(k, v):
    """
    enter item to db
    if k already define, it is override.
    :param k: key to enter
    :param v: value to enter
    :return: "ok" if it was executed correctly.
    """
    return _r_server.set(k, v)


def r_get(k: str):
    """
    get value by key.
    :param k: key
    :return: the value of key, or nil when key does not exist.
    """
    return _r_server.get(k)


def init():
    _r_server.set("ID", "0")
    _r_server.set("BirthYear", "1900")
    _r_server.set("Specialty", "")
    _r_server.set("START_MESSAGE", 1)
    _r_server.set("ID_FILL", 2)
    _r_server.set("BIRTHYEAR_FILL", 3)
    _r_server.set("SPECIALTY_FILL", 4)
    _r_server.set("connection_status", 0)
