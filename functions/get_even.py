def get_even(*args: list) -> list:
    out_lst = []
    for num in args:
        if num % 2 == 0:
            out_lst.append(num)
    return out_lst


my_list = list(map(int, input().split()))
print(get_even([my_list]))
