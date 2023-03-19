from random import choice, randint


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Ellipse:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


options = [Line, Rect, Ellipse]
elements = []
for i in range(217):
    temp_class = choice(options)
    temp_object = temp_class(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    elements.append(temp_object)

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)
