
import dbProcess
from checkTables import checkTables
from createDBtables import createAndInitTables
from createTables import createPropertiesForTables
from util.util import splitStructureRules
from util.templatesUsers import createTemplates


def generateKey(prop: object) -> tuple:
    '''
    Rules for creating key will be read and the objects
    for key inserts created. Afterwards the data will 
    be inserted into DB.
    return bool and list.
    '''

    structureRuleSplitList = splitStructureRules(prop=prop)
    if not structureRuleSplitList[0]:
        return [], structureRuleSplitList[1]

    templates = createTemplates(structureRuleSplitList=structureRuleSplitList[1])

    listOfTables = createPropertiesForTables(templates)
    if not listOfTables[0]:
        return listOfTables[0], listOfTables[1]
    else:
        listOfDBtables = createAndInitTables(listOfTables[1])

    listOfcheckedDBtables = checkTables(listOfDBtables=listOfDBtables)

    if listOfcheckedDBtables[0]:
        return listOfcheckedDBtables[0], listOfcheckedDBtables[1]
    else:
        reportDB = dbProcess(data=listOfcheckedDBtables[1], prop=prop)
        if reportDB[0]:
            return reportDB[2], None
        else:
            return reportDB[2], reportDB[1]
