def is_len_is_6(string: str) -> bool:
    return True if len(string) >= 6 else False


list_of_cities = input().split()
for city in list_of_cities:
    if is_len_is_6(city):
        print(city, end=' ')