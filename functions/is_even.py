def is_ever(value):
    return True if value % 2 == 0 else False


while True:
    n = int(input())
    if is_ever(n):
        print(n)
    if n == 1:
        break
