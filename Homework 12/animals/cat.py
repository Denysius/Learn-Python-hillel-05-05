from .animal import Animal

class Cat(Animal):
    def __init__(self, name: str, age: int, say_word='Мяуууу!'):
        """
        Класс отвечает за симуляцию животного кошки
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'рыба', 'мясо' 'молоко'}
        )
        self.animal_type = 'Кошка'

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
