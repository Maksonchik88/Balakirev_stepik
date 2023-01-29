def get_data_fig(*args, **kwargs):
    arg_lst = ['type', 'color', 'closed', 'width']
    lst = [sum(args)]
    for word in arg_lst:
        for k, v in kwargs.items():
            if word == k:
                lst.append(v)
    return tuple(lst)


print(get_data_fig(2, 55, 46, 7, color=None, closed=False, width=None, type=False, ))
print(get_data_fig(2, 55, 0, 7, type=True, color=None, closed=False, width=5))
print(get_data_fig(2, 55, 46, 7, type=False, color=7,  width=None, closed=True))
print(get_data_fig(55, 46, 7, type=True, closed=True, width=3))

