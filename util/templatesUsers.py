
from pony.orm import db_session, select
from <pathToUsersEntity> import Users
from <connectionToDBpath> import getDB


listOfWords = [
    '<modeKey>',
    '<modeKey>',
    '<modeKey>',
    '<modeKey>',
    '<modeKey>',
    '<modeKey>'
    ]


def copyItems(data: dict, forEach: list, newDataList: list, listOfWords: list) -> list:
    '''
    For every usergroup or user the copy of inputRules will be created.
    '''

    for each in forEach:
        newDict: dict = {}
        for k, v in data.items():
            if (k == listOfWords[0] or k == listOfWords[1] or k == listOfWords[2]):
                newDict[k] = [each]
            else:
                newDict[k] = v
        newDataList.append(newDict)
    return newDataList


def readUsersFromGroups(dList: dict, listOfWords: list) -> list:
    '''
    From usergroups add users into the list
    return 'listOfUsers'
    '''

    for key, value in dList.items():
        if key == listOfWords[0]: 
            with db_session:
                getUsers = Users.select(lambda p: p.usergroup == value[0])
                listOfUsers: list = []
                for user in getUsers:
                    listOfUsers.append(user.user)
            return listOfUsers


def getUserFromPers(data: list) -> list:
    '''
    Find profiles according to the field (column) in DB. 
    With nr number is searching forward for usernames.
    return 'copyPropertyForUsers'.
    '''

    values: list = []
    for ind, elem in enumerate(data[listOfWords[4]]):
        if ind == 0:
            field = elem
        elif ind > 0:
            values.append(elem)

    value: str = "'"
    for v in values:
        if len(values) == 1:
            value += v + "'"
        else:    
            value += v + "','"
    if ',' in value:
        value = value[:-2]
    value = '(' + value + ')'
    
    stmt = 'select * from pe where ' + field + ' in ' + value + ' order by ' + field

    users: list = []
    with db_session:
        getPe = getDB().select(stmt)
        for pe in getPe:
            getUser = select(
                u for u in Users
                if u.nr == pe.NR
                )[:]
            for items in getUser:
                users.append(items.user)

    del data[listOfWords[4]] 
    data[listOfWords[3]] = users
    copyPropertyForUsers: list = []
    copyPropertyForUsers.append(data)

    return copyPropertyForUsers


def createTemplates(structureRuleSplitList: list) -> list:
    '''
    The list of dict will be checked if there is need of more users.
    The users name will be added.
    Where are more groups or profiles choosen, the input data rule will be copied.
    return 'newStructureRuleSplitList'.
    '''

    newStructureRuleSplitList: list = []
    for data in structureRuleSplitList:
        for key, value in data.items():
            if (key == listOfWords[0] or key == listOfWords[1] or key == listOfWords[2]):
                if len(value) > 1:
                    newStructureRuleSplitList = copyItems(
                        data=data,
                        forEach=value,
                        newDataList=newStructureRuleSplitList,
                        listOfWords=listOfWords
                    )
                    break
                else:
                    newStructureRuleSplitList.append(data)
                    break
            elif key == listOfWords[4]:
                newStructureRuleSplitList = getUserFromPers(data)
                break
            elif key == listOfWords[5]:
                newStructureRuleSplitList.append(data)
                break

    for dList in newStructureRuleSplitList:
        if listOfWords[0] in dList:
            listOfUsers = readUsersFromGroups(
                dList=dList, 
                listOfWords=listOfWords
                )
            dList[listOfWords[3]] = listOfUsers

    return newStructureRuleSplitList