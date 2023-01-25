def is_perimeter(width: int, height: int) -> int:
    perim = (width + height) * 2
    text = f"Периметр прямоугольника, равен {perim}"
    print(text)


a, b = list(map(int, input().split()))
is_perimeter(a, b)
