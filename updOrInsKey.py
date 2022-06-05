
from <pathOfLogFunction> import Log
from pony.orm import db_session, rollback
from util.entity.key import (
    KeyK,
    Key,
    KeyS
    )

log = Log(__name__)


def updateDB(insertData):
    with db_session:
        try:
            keyK = KeyK[insertData.key]
            keyK.set(
                keytext=insertData.keytext,
            )
        except:
            rollback()
            return False, 'DB Error: no update table keyK (key <{}>).'.format(insertData.key)

        try:
            if hasattr(insertData, 'rowsKey'):
                for item in insertData.rowsKey:
                    key = Key[insertData.Ukey]
                    key.set(
                        nr=item.nr,
                        ukeytext=item.Ukeytext,
                        position=item.position,
                    )
        except:
            try:
                Key(
                    nr=item.nr,
                    ukey=item.Ukey,
                    ukeytext=item.Ukeytext,
                    position=item.position,
                )
            except:
                rollback()
                return False, 'DB Error: no update table key (key <{}>).'.format(insertData.Ukey)

        try:
            if hasattr(insertData, 'rowsKeyS'):
                for item in insertData.rowsKeyS:
                    keyS = KeyS[item.order]
                    keyS.set(
                        nr=item.nr,
                        o_position=item.o_position
                    )
        except:
            try:
                KeyS(
                    order=item.order,
                    nr=item.nr,
                    o_position=item.o_position
                )
            except:
                rollback()
                return False, 'DB Error: no update table keyS (key <{}>).'.format(insertData.order)

        log('Update successful: {}.'.format(insertData.key))
        return True, None


def insertDB(insertData):
    with db_session:
        try:
            KeyK(
                key=insertData.key,
                keytext=insertData.keytext
            )
        except:
            rollback()
            return False, 'DB Error: insert table keyK (key <{}>).'.format(insertData.key)

        try:
            if hasattr(insertData, 'rowsKey'):
                for item in insertData.rowsKey:
                    Key(
                        nr=item.nr,
                        ukey=item.Ukey,
                        ukeytext=item.Ukeytext,
                        position=item.position,
 
                    )
        except:
            rollback()
            return False, 'DB Error: insert table keyS (key <{}>).'.format(insertData.Ukey)

        try:
            if hasattr(insertData, 'rowsKeyS'):
                for item in insertData.rowsKeyS:
                    KeyS(
                        order=item.order,
                        nr=item.nr,
                        o_position=item.o_position
                    )
        except:
            rollback()
            return False, 'DB Error: insert table keyS (key <{}>).'.format(insertData.order)

        log('Insert successful: {}.'.format(insertData.key))
        return True, None

