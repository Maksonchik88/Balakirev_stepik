import sys


class StreamData:

    def create(self, fields, lst_values):
        if len(lst_values) != len(fields):
            return False
        for at, val in zip(fields, lst_values):
            setattr(self, at, val)
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
