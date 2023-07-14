from .animal import Animal
import random


class Cow(Animal):
    # init так же называют конструктором класса
    def __init__(self, name: str, age: int, say_word='Мууууууу!'):
        """
        Класс отвечает за симуляцию животного коровы
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'трава', 'сено'}
        )
        self.animal_type = 'Корова'
        self.vet_care_needed = None  # Змінна для зберігання результату перевірки

    def treat(self, hours: int) -> str:
        """
        Ухаживая за коровой должное количество времени, мы получаем молоко
        :param hours: время ухаживания
        :return: молоко или ничего
        """
        if hours > 1:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете ведро молока')
            return 'Ведро молока'
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

