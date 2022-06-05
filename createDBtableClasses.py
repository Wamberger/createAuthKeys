

class TableKeyK:
    def __init__(self, data: object, columnList: list):
        if hasattr(data, columnList[0]) and data.key and data.key.strip():
            self.key = data.key.strip()
        else:
            self.key = ' '
        if hasattr(data, columnList[1]) and data.keytext and data.keytext.strip():
            self.keytext = data.keytext.strip()
        else:
            self.keytext = ' '


class TableKey:
    def __init__(self, columnLabel: list, columns: list):
        for items in columns:
            if columnLabel[2] in items:
                if items[columnLabel[2]].replace('-','', 1).isdigit():
                    self.nr = int(items[columnLabel[2]])
                else:
                    self.nr = 0
            if columnLabel[3] in items:
                self.Ukeykey = items[columnLabel[3]].strip()
            if columnLabel[4] in items:
                self.Ukeytext = items[columnLabel[4]].strip()
            if columnLabel[5] in items:
                self.position = items[columnLabel[5]].strip()

    def initEmptyColumns(self, columnLabel: list, row: int):
        if not hasattr(self, columnLabel[2]) or not getattr(self, columnLabel[2]):
            for number in range(1, 40):
                if row == number:
                    self.nr = int(str(number) + '0')
                    break
        if not hasattr(self, columnLabel[3]) or not getattr(self, columnLabel[3]):
            self.Ukeykey = ' '
        if not hasattr(self, columnLabel[4]) or not getattr(self, columnLabel[4]):
            self.Ukeytext = ' '
        if not hasattr(self, columnLabel[5]) or not getattr(self, columnLabel[5]):
            self.position = ' '
        return self


class TableKeyS:
    def __init__(self, columnLabel: list, columns: list):
        for items in columns:
            if columnLabel[2] in items:
                if items[columnLabel[2]].replace('-','', 1).isdigit():
                    self.nr = int(items[columnLabel[2]])
                else:
                    self.nr = 0
            if columnLabel[6] in items:
                self.order = items[columnLabel[6]].strip()
            if columnLabel[7] in items:
                self.o_position = items[columnLabel[7]].strip()

    def initEmptyColumns(self, columnLabel: list, row: int):
        if not hasattr(self, columnLabel[2]) or not getattr(self, columnLabel[2]):
            for number in range(1, 40):
                if row == number:
                    self.nr = int(str(number) + '0')
                    break
        if not hasattr(self, columnLabel[6]) or not getattr(self, columnLabel[6]):
            self.order = ' '
        if not hasattr(self, columnLabel[7]) or not getattr(self, columnLabel[7]):
            self.o_position = ' '
        return self
