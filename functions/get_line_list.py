d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(lst: list, new=[]) -> list:
    for el in lst:
        if type(el) == list:
            get_line_list(el)
        else:
            new.append(el)

    return new


print(get_line_list(d))
