resp_a = "Доброго вечора, я бот з України!"
resp_b = "Вчусь програмувати на Python!"
resp_c = "Соррі, що втручаюсь, не знаю про що йдеться мова, але подивіться Рік і Морті, він просто бомба!"
resp_d = "Побачимось у мережі, I'll be back."
resp_f = "Дуже цікаво, але, нажаль, нічого не зрозуміло :("
# Переменные вывел вверх что бы сохранить время при переделке кода
print("Вітаю в боті!")

while True:
    x = input("Введіть ваше повідомлення: ")
    x = x.lower()
    # БУдем искать через find. Если find не равен -1 значит в тексте находится ключевое слово
    if x.find("привіт") != -1 or x.find("хай") != -1 or x.find("доброго дня") != -1:
        print(resp_a)
    elif x.find("як справи?") != -1 or x.find("що робиш?") != -1 or x.find("чим займаєшся?") != -1:
        print(resp_b)
    elif x.find("фільм") != -1 or x.find("кінотеатр") != -1 or x.find("серіал") != -1:
        print(resp_c)
    elif x.find("бувай") != -1 or x.find("надобраніч") != -1 or x.find("гудбай") != -1 or x.find("до зустрічі") != -1:
        print(resp_d)
        break
    else:
        print(resp_f)