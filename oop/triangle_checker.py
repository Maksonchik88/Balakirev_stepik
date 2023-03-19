class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        all_int_or_float = all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c)))
        if not all_int_or_float:
            return 1

        all_more_than_zero = all(map(lambda x: x > 0, (self.a, self.b, self.c)))
        if not all_more_than_zero:
            return 1

        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.a + self.b:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
