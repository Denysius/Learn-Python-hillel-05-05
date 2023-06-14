def remove_brackets(user_text):
    user_text = input()
    while user_text != "exit":
        open_brackets = user_text.find("(")
        close_brackets = user_text.find(")")
    if open_brackets != -1 and close_brackets != -1:
        user_text = user_text[:open_brackets] + user_text[close_brackets+1:]
        print("Відредагований текст:", remove_brackets)
        user_text = input("Введіть свій текст на редагування (або введіть 'exit' для виходу): ")
    return user_text
user_text = input("Введіть свій текст на редагування (або введіть 'exit' для виходу): ")
remove_brackets(user_text)


