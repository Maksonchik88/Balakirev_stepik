def is_large(my_str: str) -> bool:
    return True if len(my_str) >= 3 else False



str_for_check = input()
print(is_large(str_for_check))