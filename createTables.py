
from util.util import updateInputVariablesWithDBvalues

stringNames = [
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>',
    '<someKeyWordsOrErrorWarningMsg>'
]


def createPropertiesForTables(templates: list) -> tuple:
    '''
    Input data will be sorted, init and prepared before it generates class of DB rows.
    '''
    
    mainDataList = updateInputVariablesWithDBvalues(
        templates=templates,
        stringNames=stringNames
        )
    if not mainDataList[0]:
        return mainDataList[0], mainDataList[1]
    else:
        mainDataList = mainDataList[1]

    class TemplateTable:
        def __init__(self) -> None:
            pass

    listOfRows = []
    for listInList in mainDataList:
        templateTable = TemplateTable()
        for dictItems in listInList:
            if stringNames[0] in dictItems:
                setattr(templateTable,
                        stringNames[0], dictItems[stringNames[0]])
            if stringNames[1] in dictItems:
                setattr(templateTable,
                        stringNames[1], dictItems[stringNames[1]])
            if hasattr(templateTable, stringNames[0]) and hasattr(templateTable, stringNames[1]):
                break
        if templateTable:
            rowDict = {}
            for dictItems in listInList:
                for key, value in dictItems.items():
                    if key in stringNames:
                        break
                    if not key in rowDict:
                        tmpList = []
                    tmpList.append(value)
                    rowDict[key] = tmpList
            setattr(templateTable, stringNames[9], rowDict)
            listOfRows.append(templateTable)

    return True, listOfRows
