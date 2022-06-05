

from pony.orm import db_session
from util.entity.key import KeyK
from updOrInsKey import updateDB, insertDB

def dbProcess(data: list) -> tuple:

    for items in data:
        with db_session:
            checkKey = KeyK.get(key=items.key)
        if checkKey:
            report = updateDB(items)
            if not report[0]:
                return report[0], report[1], data
        else:
            report = insertDB(items)
            if not report[0]:
                return report[0], report[1], data
    return True, None, data
