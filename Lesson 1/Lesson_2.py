import math
direction = input("Виберіть напрямок конвертації (rad - градуси в радіани, deg - радіани в градуси): ")
if direction == "rad":
x: =float(input('Введите градус для пересчета в радианы'))
y= x*math.pi/180
print(y)
elif direction == "deg":
x = float(input('Введите радианы для пересчета в градусы'))
y= x*180/math.pi
print(y)

else:
print("Помилка!!! Невірний напрямок конвертації")
