
import inspect
from pony.orm import db_session
from <pathToEntity> import Users
from <pathToEntity> import Pe
from <pathToFunction> import substituteTemplateStr

keyColumnList = [
    'key',
    'keytext',
    'nr',
    'Ukey',
    'Ukeytext',
    'position',
    'order',
    'o_position'
]


def splitStructureRules(prop: object) -> tuple:
    '''
    The input data comes as string in object attribute.
    The string will be divided into dict with list as values 
    according to the sign (& $ ,) cuts.
    Return bool and list of dict.
    '''
    
    try:
        firstSplit = [l for l in prop.structureRule.split('&')]
        structureRuleSplitList: list = []
        for eachSplit in firstSplit:
            secondSplit = [l.split('=') for l in eachSplit.split('$')]
            dictRules: dict = {}
            for elem in secondSplit:
                dictRules[elem[0]] = [x for x in elem[1].split(',')]
            structureRuleSplitList.append(dictRules)
        
        return True, structureRuleSplitList

    except:
        return False, 'Wrong params: {}.'.format(prop.structureRule)


def createDictFromDBtablesWithValues(*argv) -> dict:
    """
    input object classes, output dictionary.
    It get column names from objects and then creates 
    dictionary with column names as keys with 
    the values from the objects attributes. 
    """

    dataList: dict = {}
    for argInTuple in argv:
        if argInTuple:
            for getColNames in inspect.getmembers(argInTuple):
                tableColumnNames = getColNames[1]._columns_
                break
            for columnName in tableColumnNames:
                if hasattr(argInTuple, columnName.lower()):
                    value = getattr(argInTuple, columnName.lower())
                    dataList[columnName.lower()] = value
    return dataList


def fillData(user: str, elements: dict, stringNames: list) -> tuple:
    '''
    If there is a column name inside {{}} from the DB, 
    it will be replaced with the values from DB.
    return bool and list of dicts.
    '''

    tmpList: list = []
    for key, value in elements.items():
        if isinstance(value, list):
            for text in value:
                dictItems: dict = {}
                if (key == stringNames[2] or key == stringNames[3]):
                    dictItems[stringNames[7]] = user
                    tmpList.append(dictItems)
                    break
                elif '{{' in text:
                    try:
                        with db_session:
                            getUserData = Users.get(user=user)
                            getPersData = Pe.get(
                                persnr=getUserData.nr)
                            dataWithValuesAndKeys = createDictFromDBtablesWithValues(
                                getPersData,
                                getUserData
                            )
                            newText = substituteTemplateStr(
                                templateStr=text,
                                params=dataWithValuesAndKeys
                            )
                            dictItems[key] = newText
                    except:
                        return False, stringNames[8].format(user)
                else:
                    dictItems[key] = text
                tmpList.append(dictItems)
        else:
            typeOf = type(value)
            return False, stringNames[6].format(typeOf)
    return True, tmpList


def updateInputVariablesWithDBvalues(templates: list, stringNames: list) -> tuple:
    '''
    Loop through templates(list) and go for every user into another 
    function (fillData) where they init values. 
    In mode usergroup no init of values can happen, because the user nr is not know.
    return bool and list of dict.
    '''

    mainDataList: list = []
    for elements in templates:
        for key, value in elements.items():
            if stringNames[2] == key: 
                for user in value:
                    listDictItems = fillData(
                        user=user, 
                        elements=elements, 
                        stringNames=stringNames
                        )
                    if listDictItems[0]:
                        mainDataList.append(listDictItems[1])
                    else:
                        return listDictItems[0], listDictItems[1]
            elif (stringNames[3] == key): 
                tmpList: list = []
                for key1, value1 in elements.items():
                    if isinstance(value1, list):
                        for text in value1:
                            dictItems = {}
                            if '{{' in text:
                                return False, stringNames[4]
                            else:
                                dictItems[key1] = text
                            tmpList.append(dictItems)
                    else:
                        typeOf = type(value1)
                        return False, stringNames[5].format(typeOf)
                mainDataList.append(tmpList)
                break

    return True, mainDataList