
from pony.orm import PrimaryKey, Required
from <pathToDBConnection> import getDB


class KeyK(getDB().Entity):
    _table_ = "KEYK"
    key = PrimaryKey(str)
    keytext = Required(str)

class Key(getDB().Entity):
    _table_ = "KEY"
    nr = Required(int)
    Ukey = PrimaryKey(str)
    Ukeytext = Required(str)
    position = Required(str)

class KeyS(getDB().Entity):
    _table_ = "KEYS"
    nr = Required(int)
    order = PrimaryKey(str)
    o_position = Required(str)
    