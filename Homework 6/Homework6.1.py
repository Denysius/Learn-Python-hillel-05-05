def remove_brackets(user_text):
    while True:
        open_brackets = user_text.find("(")
        close_brackets = user_text.find(")")

        if open_brackets != -1 and close_brackets != -1:
            user_text = user_text[:open_brackets] + user_text[close_brackets + 1:]
        else:
            break

    print("Відредагований текст:", user_text)


user_input = input("Введіть свій текст на редагування (або введіть 'exit' для виходу): ")
while user_input != "exit":
    remove_brackets(user_input)
    user_input = input("Введіть свій текст на редагування (або введіть 'exit' для виходу): ")
else:
    print('Ви вийшли')
