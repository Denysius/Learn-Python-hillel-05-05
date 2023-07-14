from animals import Dog, Hen, Cow, Cat
from random import choices, randint

if __name__ == '__main__':
    animals = [
        Dog('Жучка', 3),
        Hen('Коко', 2),
        Cow('Милка', 5),
        Cat('Мурзик', 2)
    ]

    available_food = ['сено', 'трава', "зерно", "пшено", "каша", "мясо", "кость", "тортик", "молоко"]

    what_we_got = list()
    what_we_lost = list()
    for animal in animals:
        animal.say()
        animal.needs_vet_care()  # Доданий виклик методу needs_vet_care()
        animals_needing_care = [animal for animal in animals if animal.needs_vet_care()]
        if animals_needing_care:
            print("Тварини, які потребують догляду ветеринара:")
            for animal in animals_needing_care:
                print(animal)
        else:
            print("Немає тварин, які потребують догляду ветеринара.")
        """ то же самое, что и ниже
        for i in range(3):
            food = choice(available_food)
            animal.eat(food)
        """
        for food in choices(available_food, k=6):
            what_we_lost.append(food)
            animal.eat(food)
        if animal.hungry:
            print(f'{animal} голодает! Покормите его.')
        what_we_got.append(animal.treat(randint(0, 5)))
        print('=' * 20)

    print(f'Сегодня на ферме мы потратили: {", ".join(what_we_lost)} и получили {", ".join(what_we_got)}')