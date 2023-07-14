from .animal import Animal
import random


class Dog(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Гав-гав!'
    ):
        """
        Класс отвечает за симуляцию животного собака
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'каша', 'мясо', 'кость'}
        )
        self.animal_type = 'Собака'
        self.vet_care_needed = None  # Змінна для зберігання результату перевірки

    def treat(self, hours: int) -> str:
        """
        Ухаживая за собакой должное количество времени, мы получаем хорошее настроение
        :param hours: сколько часов ухаживаем
        :return: ничего или хорошее настроение
        """
        if hours > 2:
            print(f'Вы гуляете с {self} {hours} часов и у вас повышается настроение')
            return 'Хорошее настроение'
        print(f'Вы гуляете с {self} {hours} часов.')
        return ''

    def needs_vet_care(self) -> bool:
        """
        Метод перевіряє, чи потрібно до ветеринара
        :return: True, якщо потрібно до ветеринара, False - якщо ні
        """
        if self.vet_care_needed is None:  # Перевіряємо, чи була вже виконана перевірка
            self.vet_care_needed = random.choice([True, False])  # Рандомно встановлюємо результат перевірки
        return self.vet_care_needed
