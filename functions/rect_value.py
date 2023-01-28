def get_rect_value(a: int, b: int, type=0) -> int:
    if type == 0:
        return ((a + b) * 2)
    else:
        return a * b


print(get_rect_value(4, 5))
