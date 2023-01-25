def is_triangle(a, b, c) -> bool:
    if a < (b + c) and b < (a + c) and c < (a + b):
        return True
    else:
        return False


x, y, z = list(map(int, input().split()))

print(is_triangle(x, y, z))