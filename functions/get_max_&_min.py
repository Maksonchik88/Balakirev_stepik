def get_max_and_min(num_1: int, num_2: int) -> int:
    return num_1 * num_2


numbers_lst = list(map(int, input().split()))
max_num = max(numbers_lst)
min_num = min(numbers_lst)

print(get_max_and_min(max_num, min_num))