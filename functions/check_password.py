def check_password(code: str, chars="$%!?@#") -> bool:
    for ch in code:
        if ch in chars and len(code) > 7:
            return True
    else:
        return False


my_str = input()
print(check_password(my_str))
