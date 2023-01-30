def get_rec_N(num: int) -> int:
    if num > 0:
        get_rec_N(num - 1)
        print(num)


N = int(input())
get_rec_N(N)