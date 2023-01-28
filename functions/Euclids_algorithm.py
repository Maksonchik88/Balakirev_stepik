def get_nod(a: int, b: int) -> int:
    while b != a:
        if a > b:
            a -= b
        else:
            b -= a

    return a


my_lst = list(map(int, input().split()))
num_1 = int(my_lst[0])
num_2 = int(my_lst[1])

print(get_nod(num_1, num_2))
