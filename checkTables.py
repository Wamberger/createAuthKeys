

from util.util import keyColumnList
from checkTablesDef import (
    checkKey,
    checkKeyK,
    checkKeyS
    )

errorMessages = [
    '<errorMessage>',
    '<errorMessage>',
    '<errorMessage>',
    '<errorMessage>',
    '<errorMessage>'
]


def checkTables(listOfDBtables: list) -> tuple:

    for data in listOfDBtables:
        report = checkKeyK(
            data=data,
            columns=keyColumnList,
            errorMessages=errorMessages
        )
        if report[0]:
            return report[0], report[1]

        for row in data.rowsKey:
            report = checkKey(
                data=row,
                columns=keyColumnList,
                errorMessages=errorMessages
            )
            if report[0]:
                return report[0], report[1]

        for row in data.rowsKeyS:
            report = checkKeyS(
                data=row,
                columns=keyColumnList,
                errorMessages=errorMessages
            )
            if report[0]:
                return report[0], report[1]

    return False, listOfDBtables
