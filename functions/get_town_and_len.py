def get_town_and_len(string: str) -> tuple:
    tuple_for_return = (string,len(string))
    return tuple_for_return


lst_of_cities = input().split()
my_dict = {}
for city in lst_of_cities:
    my_dict[get_town_and_len(city)[0]] = get_town_and_len(city)[1]

my_dict_sort = sorted(my_dict, key=lambda x: my_dict[x])
print(*my_dict_sort)