def get_rec_sum(lst: list) -> int:
    return sum(lst)


my_list = list(map(int, input().split()))
print(get_rec_sum(my_list))
