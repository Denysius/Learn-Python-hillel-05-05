import random


class Cat:
    def __init__(self, name, age, breed, preferred_food):
        """
        Класс кішка
        :param name: ім'я
        :param age: вік
        :param breed: порода
        :param preferred_food: їжа
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food
        self.hungry = True
        self.hours_outdoors = 0

    def __str__(self):
        starting_str = f"{self.breed.capitalize()} {self.name}, {self.age} "
        if self.age == 1:
            starting_str += "рік"
        elif 2 <= self.age <= 4:
            starting_str += "роки"
        else:
            starting_str += "років"
        starting_str += f", годин гуляла: {self.hours_outdoors}, голодна: {self.hungry}"
        return starting_str

    def meow(self):
        print(f"{self.name} м'яукає: Мяу!")

    def eat(self, food):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} їсть {food}")
                self.hungry = False
            else:
                print(f"{self.name} не їсть таке: {food}")
                self.meow()
        else:
            print(f"{self.name} не голодна")

    def walk(self):
        hours = random.randint(1, 3)
        print(f"{self.name} гуляє сама {hours} годин")
        self.hours_outdoors += hours
        if self.hours_outdoors > 3:
            self.hungry = True


if __name__ == '__main__':
    cats = [
        Cat('Барсик', 2, 'дворова', {'риба', 'каша'}),
        Cat('Мурка', 3, 'шотландська', {'сметана', 'паштет', 'рис'}),
        Cat('Рижик', 4, 'сфінкс', {'сухі корми', 'суші', 'бургер'}),
        Cat('Леопольд', 1, 'сіамська', {'вугор', 'каша', 'цукерки'}),
        Cat('Сімка', 5, 'британська', {'молоко', 'риба', 'шашлик'}),
        Cat('Василиса', 2, 'мейн-кун', {'кролик', 'курятина'}),
    ]

    for day in range(1, 8):
        print(f"День {day}")
        for cat in cats:
            cat.walk()
            potential_food = ['сухі корми', 'паштет', 'риба', 'вугор', 'каша', 'молоко', 'кролик', 'курятина',
                              'бургер', 'шашлик', 'рис', 'суші', 'цекерки']
            random_food = random.choice(potential_food)
            cat.eat(random_food)
            print(cat)
        print('=' * 55)
