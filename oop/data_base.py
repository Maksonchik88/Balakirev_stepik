import sys
from typing import List, Dict

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a: int, b: int) -> List[Dict]:
        return self.lst_data[a:b + 1]

    def insert(self, data: list):
        for line in data:
            self.lst_data.append(dict(zip(self.FIELDS, line.split())))


db = DataBase()
db.insert(lst_in)
