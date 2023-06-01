print("Вітаю! Введіть слово:")
x = input()
x = x.lower()
punctuations = (' ', '+', '-', '=', '*', '/', '.', ',', '?', '!')
print("Іде перевірка рядка:")
for symbol in punctuations:
    x = x.replace(symbol, "")
if x == x[::-1]:
    print("Це поліндромний рядок")
else:
    print("Це не поліндромний рядок")
