print("Доброго вечора! Введіть свій текст на редагування:\n")
x = input()
# Задаємо умову для пошуку індексів дужок на відкриття та закриття
open_brackets = x.find("(")
close_brackets = x.find(")")
# Використовуємо слайсінг для видалення тексту в дужках
if open_brackets != -1 and close_brackets != -1:
    Redact = x[:open_brackets] + x[close_brackets+1:]
else:
    Redact = x
print(Redact)
