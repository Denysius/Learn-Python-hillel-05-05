def word_gen():
    s = input("Введіть рядок: ")
    words = s.split()
    for word in words:
        yield word

    if __name__ == '__main__':
        generator = word_gen()
        for word in generator:
            print(word)
