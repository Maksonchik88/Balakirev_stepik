def get_tag_up(my_str: str, tag="div", up=True) -> str:
    if up:
        tag = tag.upper()
        res = f"<{tag}>{my_str}</{tag}>"
        return res
    else:
        res = f"<{tag}>{my_str}</{tag}>"
        return res


str_input = input()
print(get_tag_up(str_input))
print(get_tag_up(str_input, up=False))
