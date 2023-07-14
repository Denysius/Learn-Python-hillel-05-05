from .animal import Animal
import random
class Cat(Animal):
    def __init__(self, name: str, age: int, say_word='Мяуууу!'):
        """
        Класс отвечает за симуляцию животного кошки
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'рыба', 'мясо', 'молоко'}
        )
        self.animal_type = 'Кошка'
        self.vet_care_needed = None  # Змінна для зберігання результату перевірки

    def treat(self, hours: int) -> str:
        """
        Ухаживая за кошкой должное количество времени, мы получаем пойманых мышей
        :param hours: время ухаживания
        :return: мышь или ничего
        """
        if hours > 1:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете пойманых мышей')
            return 'Пойманых мышей'
        print(f'Вы ухаживаете за {self} {hours} часов.')
        return ''

    def needs_vet_care(self) -> bool:
        """
        Метод перевіряє, чи потрібно до ветеринара
        :return: True, якщо потрібно до ветеринара, False - якщо ні
        """
        if self.vet_care_needed is None:  # Перевіряємо, чи була вже виконана перевірка
            self.vet_care_needed = random.choice([True, False])  # Рандомно встановлюємо результат перевірки
        return self.vet_care_needed