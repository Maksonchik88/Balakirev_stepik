def fact_rec(num: int)-> int:
    if num == 0:
        return 1
    else:
        return fact_rec(num - 1) * num

n = int(input())
print(fact_rec(n))