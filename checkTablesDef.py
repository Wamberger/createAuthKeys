
def checkKeyK(data: object, columns: list, errorMessages: list):
    for key, value in data.__dict__.items():
        if (isinstance(value, str) and not value) or value is None:
            return True, errorMessages[0].format(key, value)

    if not isinstance(data.key, str):
        return True, errorMessages[1].format(columns[0], data.key)
    elif data.key.isspace():
        return True, errorMessages[0].format(columns[0], data.key)
    elif len(data.key) > 10:
        return True, errorMessages[2].format(columns[0], len(data.key), data.key)

    if not isinstance(data.keytext, str):
        return True, errorMessages[1].format(columns[1], data.keytext)
    elif data.keytext.isspace():
        return True, errorMessages[0].format(columns[1], data.keytext)
    elif len(data.keytext) > 60:
        return True, errorMessages[2].format(columns[1], len(data.keytext), data.keytext)

    return False, None


def checkKey(data: object, columns: list, errorMessages: list):
    for key, value in data.__dict__.items():
        if (isinstance(value, str) and not value) or value is None:
            return True, errorMessages[0].format(key, value)

    if not isinstance(data.nr, int):
        return True, errorMessages[3].format(columns[2], data.nr)
    elif data.nr == 0:
        return True, errorMessages[0].format(columns[2], data.nr)
    elif data.nr > 99999:
        return True, errorMessages[4].format(columns[2], data.nr, data.nr)

    if not isinstance(data.Ukey, str):
        return True, errorMessages[1].format(columns[3], data.Ukey)
    elif len(data.Ukey) > 10:
        return True, errorMessages[2].format(columns[3], len(data.Ukey), data.Ukey)

    if not isinstance(data.Ukeytext, str):
        return True, errorMessages[1].format(columns[4], data.Ukeytext)
    elif len(data.Ukeytext) > 500:
        return True, errorMessages[2].format(columns[4], len(data.Ukeytext), data.Ukeytext)

    if not isinstance(data.position, str):
        return True, errorMessages[1].format(columns[5], data.position)
    elif len(data.position) > 4:
        return True, errorMessages[2].format(columns[5], len(data.position), data.position)

    return False, None


def checkKeyS(data: object, columns: list, errorMessages: list):
    for key, value in data.__dict__.items():
        if (isinstance(value, str) and not value) or value is None:
            return True, errorMessages[0].format(key, value)

    if not isinstance(data.nr, int):
        return True, errorMessages[3].format(columns[2], data.nr)
    elif data.nr == 0:
        return True, errorMessages[0].format(columns[2], data.nr)
    elif data.nr > 99999:
        return True, errorMessages[4].format(columns[2], data.nr, data.nr)

    if not isinstance(data.order, str):
        return True, errorMessages[1].format(columns[6], data.order)
    elif data.order.isspace():
        return True, errorMessages[0].format(columns[6], data.order)
    elif len(data.order) > 10:
        return True, errorMessages[2].format(columns[6], len(data.order), data.order)

    if not isinstance(data.o_position, str):
        return True, errorMessages[1].format(columns[7], data.o_position)
    elif len(data.o_position) > 4:
        return True, errorMessages[2].format(columns[7], len(data.o_position), data.o_position)

    return False, None
