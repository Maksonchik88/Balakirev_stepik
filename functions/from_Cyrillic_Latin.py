dict_of_symbols = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
                   'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
                   'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
                   'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def from_cyrillic_latin(cyr_str: str, sep='-') -> str:
    cyr_str = cyr_str.lower()
    latin_lst = []
    for sym in cyr_str:
        if sym in dict_of_symbols:
            latin_lst.append(dict_of_symbols[sym])
        elif sym == ' ':
            latin_lst.append(sep)
        else:
            latin_lst.append(sym)

    latin_str = "".join(latin_lst)

    return latin_str


input_str = input()
print(from_cyrillic_latin(input_str))
print(from_cyrillic_latin(input_str, sep='+'))
