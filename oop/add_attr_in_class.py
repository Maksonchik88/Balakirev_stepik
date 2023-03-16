class Person:
    name: str = 'Сергей Балакирев'
    job: str = 'Программист'
    city: str = 'Москва'


p1 = Person()
print(True if 'job' in p1.__dict__ else False)