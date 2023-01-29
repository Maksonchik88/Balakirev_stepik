def get_biggest_city(*args):
    temp_len = 0
    town = ''
    for i in args:
        if len(i) > temp_len:
            temp_len = len(i)
            town = i


    return town



input_lst = input().split()
print(get_biggest_city(*input_lst))
