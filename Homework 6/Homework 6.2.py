def positive_number():
    while True:
        number = float(input("Введіть додатнє число: "))
        if number > 0:
            return number
        else:
            print("Некоректне число. Спробуйте ще раз.")


def triangle_exist(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def perimeter(a, b, c):
    p = a + b + c
    return p


def Area(a, b, c):
    import math
    # Використаємо формулу Герона для обчислення площі трикутника
    half_p = perimeter / 2
    S = math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
    return S


# Головна частина
a = positive_number()
b = positive_number()
c = positive_number()

if triangle_exist(a, b, c):
    print("Трикутник існує.")
    perimeter = perimeter(a, b, c)
    print("Периметр трикутника:", perimeter)
    S = Area(a, b, c)
    print("Площа трикутника:", round(S, 4))
else:
    print("Трикутник не існує.")
