from operator import *
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

lst = list(map(int, input().split()))
tuple_list = filter_lst(lst)
print(*tuple_list)
only_neg = filter_lst(lst, key=lambda x: lt(x, 0))
print(*only_neg)
only_pos = filter_lst(lst, key=lambda x: ge(x, 0))
print(*only_pos)
in_the_range = filter_lst(lst, key=lambda x:  x in range(3, 6))
print(*in_the_range)