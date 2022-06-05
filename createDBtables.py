
from util.util import keyColumnList
from createDBtableClasses import (
    TableKey,
    TableKeyK,
    TableKeyS
    )

def createAndInitTables(listOfTables: list) -> list:

    listOfinserts = []
    for listOfItems in listOfTables:
        table = TableKeyK(data=listOfItems, columnList=keyColumnList)
        listItems = {}
        if listOfItems.tables:
            for key, value in listOfItems.tables.items():
                for index, item in enumerate(value, start=1):
                    if str(index) in listItems:
                        listItems[str(index)] += [{key: item}]
                    else:
                        listItems[str(index)] = [{key: item}]
        if listItems:
            listOfRows = []
            for row, columns in listItems.items():
                tableKey = TableKey(
                    columnLabel=keyColumnList,
                    columns=columns
                )
                if tableKey.__dict__:
                    tableKey.initEmptyColumns(
                        columnLabel=keyColumnList,
                        row=int(row)
                    )
                    listOfRows.append(tableKey)
            setattr(table, 'rowsKey', listOfRows)

            listOfRows = [] 
            for row, columns in listItems.items():
                tableKeyS = TableKeyS(
                    columnLabel=keyColumnList,
                    columns=columns
                )
                if tableKeyS.__dict__:
                    tableKeyS.initEmptyColumns(
                        columnLabel=keyColumnList,
                        row=int(row)
                    )
                    listOfRows.append(tableKeyS)
            setattr(table, 'rowsKeyS', listOfRows)
        listOfinserts.append(table)

    return listOfinserts
