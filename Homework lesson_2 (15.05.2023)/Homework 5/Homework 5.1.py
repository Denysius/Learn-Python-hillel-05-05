print("Вітаю! Введіть слово:\n>")
x = input()
x = x.lower()
punctuations = (' ', '+', '-', '=', '*', '/', '.', ',', '?', '!')
print("Іде перевірка рядка:")
for symbol in punctuations:
    x = x.replace(symbol, "")
# перевели рядок у нижній регістр та видалили означені символи
# Перевіряємо чи сходиться перевернуте слово з основою
if x == x[::-1]:
    print("Це поліндромний рядок")
else:
    print("Це не поліндромний рядок")
