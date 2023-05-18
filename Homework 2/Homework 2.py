import string

print('Вітаю! Давайте познайомимось, роскажіть трішки про себе:')
Introduction = input()      #Вводим начальный текст
print("Йде перевірка на зайві символи...")
Introduction_Clear = Introduction.translate(str.maketrans({key: None for key in string.punctuation}))
print("йде перевірка на зайві пробели у кінці рядка...")
Text = Introduction_Clear.rstrip()
Ready_Text = Text.lower()
print("Увага! Тексте форматовано у нижній регістр. Вивід на екран:")
print(Ready_Text)
Replaced_Word = input("Введіть слово, яке потрібно замінити:")
index = Ready_Text.find(Replaced_Word)
Replaced_to = input("Введіть слово на заміну(Для коректної роботи використовувати лише нижній регістр):")
Final_Text = Ready_Text.replace(Replaced_Word, Replaced_to)
print("Виводимо на екран:")
print(Final_Text)
