def fibonacci_generator(end_index):
    a, b = 0, 1

    for _ in range(end_index):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fibonacci_sequence = fibonacci_generator(15)
    for number in fibonacci_sequence:
        print(number)
