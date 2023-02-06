def get_path(num: int) -> int:
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return get_path(num - 1) + get_path(num - 2)


n = int(input())
print(get_path(n))
