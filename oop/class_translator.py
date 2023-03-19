from typing import List, Dict


class Translator:
    def __init__(self):
        self.my_dict: Dict = {}

    def add(self, eng: str, rus: str) -> None:
        if eng not in self.my_dict:
            self.my_dict[eng] = []
        self.my_dict[eng].append(rus)

    def remove(self, eng: str) -> None:
        if eng in self.my_dict.keys():
            self.my_dict.pop(eng, False)

    def translate(self, eng: str) -> List:
        if eng in self.my_dict.keys():
            return self.my_dict[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")

print(*tr.translate("go"))
