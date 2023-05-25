sum_key = "sum"
i = []

while True:
    x = input("Введіть число або 'sum' для отримання суми: ")

    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        y = float(x)
        i.append(y)
    else:
        print("Некоректне введення! Введіть число або 'sum'.")

    if x.lower() == sum_key:
        break

if len(i) > 0:
    result = sum(i)
    print("Сума введених чисел: ", result)

else:
    print("Числа не було введено.")
