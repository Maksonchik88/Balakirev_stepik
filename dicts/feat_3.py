st = input().split()
d = {}
for el in st:
    k, v = el.split('=')
    d[k] = int(v)

print(*sorted(d.items()))