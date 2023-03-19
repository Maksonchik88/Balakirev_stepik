"""
для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU;
total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на
материнской плате в виде следующего списка из четырех строк:
['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.
"""


class CPU:
    def __init__(self, name: str, fr: float):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: CPU, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(args[:self.total_mem_slots])

    def get_config(self):
        result = [f"Материнская плата: {self.name}", f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                  f"Слотов памяти: {len(self.mem_slots)}"]
        temp = []
        for slot in self.mem_slots:
            temp.append(f"{slot.name} - {slot.volume}")
        result.append(f"Память: {'; '.join(temp)}")
        return result


# if __name__ == '__main__':
cpu = CPU("i7", 3.2)
mem1 = Memory("kingston", 8)
mem2 = Memory("kingston", 8)
mb = MotherBoard("z490", cpu, mem1, mem2)

print(mb.get_config())
