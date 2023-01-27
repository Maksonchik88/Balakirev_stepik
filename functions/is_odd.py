def is_odd(numbers: list) -> list:
    sort_lst = []
    for el in numbers:
        if el % 2 != 0:
            sort_lst.append(el)
        else:
            continue

    return sort_lst


num = list(map(int, input().split()))

print(*is_odd(num))
