temp = input().strip()
check_word = 'RECT'
if temp == check_word:
    def get_sq(length: float, width: float) -> float:
        return length * width
else:
    def get_sq(length: float) -> float:
        return length ** 2