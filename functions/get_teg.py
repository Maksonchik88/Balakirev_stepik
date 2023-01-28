def get_tag(my_str: str, tag="h1") -> str:
    res = f"<{tag}>{my_str}</{tag}>"
    return res


str_input = input()
print(get_tag(str_input))
print(get_tag(str_input, tag="div"))