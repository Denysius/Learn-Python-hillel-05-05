import time


def add_new_note():
    """
       Функція для додавання нової нотатки.
       Користувач вводить текст нотатки, яка додається до списку нотаток.
       """
    user_input = input("Введіть нотатку: ")
    timecounter = time.time()
    note = {"text": user_input, "time": timecounter}
    notes.append(note)


def sort_by_time(note):
    """
        Функція для сортування нотаток за значенням time.
        Використовується в функціях сортування, як ключ для порівняння нотаток за часом.
        """
    return note["time"]


def sort_by_text_length(note):
    """
        Функція для сортування нотаток за довжиною тексту.
        Використовується в функціях сортування, як ключ для порівняння нотаток за довжиною.
        """
    return len(note["text"])


def show_all_from_first():
    """
        Функція для виведення нотаток у хронологічному порядку - від найранішої до найпізнішої.
        Спочатку сортуємо нотатки за часом, потім виводимо їх текст.
        """
    sorted_notes = sorted(notes, key=sort_by_time)
    print("Виведення нотаток від найранішої до найпізнішої:")
    for note in sorted_notes:
        print(note["text"])


def show_all_from_last():
    """
        Функція для виведення нотаток у хронологічному порядку - від найпізнішої до найранішої.
        Спочатку сортуємо нотатки за часом у зворотному порядку, потім виводимо їх текст.
        """
    sorted_notes = sorted(notes, key=sort_by_time, reverse=True)
    print("Виведення нотаток від найпізнішої до найранішої:")
    for note in sorted_notes:
        print(note["text"])


def show_all_from_longest():
    """
        Функція для виведення нотаток у порядку їх довжини - від найдовшої до найкоротшої.
        Спочатку сортуємо нотатки за довжиною тексту у зворотному порядку, потім виводимо їх.
        """
    sorted_notes = sorted(notes, key=sort_by_text_length, reverse=True)
    print("Виведення нотаток від найдовшої до найкоротшої:")
    for note in sorted_notes:
        print(note["text"])


def show_all_from_shortest():
    """
        Функція для виведення нотаток у порядку їх довжини - від найкоротшої до найдовшої
        Спочатку сортуємо нотатки за довжиною тексту, потім виводимо їх.
        """
    sorted_notes = sorted(notes, key=sort_by_text_length)
    print("Виведення нотаток від найкоротшої до найдовшої:")
    for note in sorted_notes:
        print(note["text"])


if __name__ == '__main__':
    commands = {
        "add": add_new_note,
        "earliest": show_all_from_first,
        "latest": show_all_from_last,
        "longest": show_all_from_longest,
        "shortest": show_all_from_shortest
    }
    notes = []
    while True:
        print("Список команд: add, earliest, latest, longest, shortest")
        print("Введіть команду:")
        command = input("> ")

        if command in commands:
            commands[command]()
        else:
            print("Невідома команда. Будь ласка, спробуйте ще раз.")
