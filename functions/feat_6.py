def is_function(my_list: list) -> str:
    my_max = max(my_list)
    my_min = min(my_list)
    my_sum = sum(my_list)
    text = f"Min = {my_min}, max = {my_max}, sum = {my_sum}"
    print(text)


lst = [int(num) for num in input().split()]
is_function(lst)