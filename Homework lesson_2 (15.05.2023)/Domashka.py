import math

direction = input("Виберіть напрямок конвертації (1 - градуси в радіани, 2 - радіани в градуси): ")

if direction == "1":
    x = float(input("Введіть значення в градусах: "))
    y = x * math.pi / 180
    print(f"{x} градусів = {round(y, 5)} радіан")
elif direction == "2":
    y = float(input("Введіть значення в радіанах: "))
    x = y * 180 / math.pi
    print(f"{y} радіан = {round(x, 5)} градусів")
else:
    print("Неправильний вибір напрямку конвертації.")