def simple_number(num):
    simple_library = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    if num in simple_library:
        return True
    else:
        return False

# # Вхідні параметри
if __name__ == '__main__':
    input_number = int(input("Введіть ціле число (до 100): "))
    simple = simple_number(input_number)
    print(simple)
