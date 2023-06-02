print("Доброго вечора! Введіть свій текст на редагування (або введіть 'exit' для виходу):\n")
x = input()
# Задаємо умову для пошуку індексів дужок на відкриття та закриття а також на вихід
while x != "exit":
    open_brackets = x.find("(")
    close_brackets = x.find(")")
# Використовуємо слайсінг для видалення тексту в дужках і продовжуємо цикл
    if open_brackets != -1 and close_brackets != -1:
        x = x[:open_brackets] + x[close_brackets+1:]
        continue
    print("Відредагований текст:", x)

    print("Введіть свій текст на редагування (або введіть 'exit' для виходу):")
    x = input()
