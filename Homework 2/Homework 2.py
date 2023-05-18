import string

print('Вітаю! Давайте познайомимось, роскажіть трішки про себе:')
#   Вводим начальный текст
Introduction = input()
#   Удаляем лишние символы
Introduction_Clear = Introduction.translate(str.maketrans({key: None for key in string.punctuation}))
#   Удаляем лишние пробелы в конце
Text = Introduction_Clear.rstrip()
#   Перевод в нижний регистр
Ready_Text = Text.lower()
print("Увага! Текст відформатовано згідно умов. Вивід на екран:")
print(Ready_Text)
Replaced_Word = input("Введіть слово, яке потрібно замінити(Для коректної роботи використовувати лише нижній регістр):")
Replaced_to = input("Введіть слово на заміну(Для коректної роботи використовувати лише нижній регістр):")
Final_Text = Ready_Text.replace(Replaced_Word, Replaced_to)
print("Виводимо на екран:")
print(Final_Text)
