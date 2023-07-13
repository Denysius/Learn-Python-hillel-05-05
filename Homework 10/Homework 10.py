import csv

def read_tech_inventory(file_path):
    tech_data = {}
    category_index = {}
    brand_index = {}

    # Генеруємо унікальний ID
    def generate_unique_id():
        id_counter = 1
        while True:
            yield id_counter
            id_counter += 1

    unique_id_generator = generate_unique_id()

    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            model = row['model']
            category = row['category']
            brand = row['brand']
            price = float(row['price'])

            # Генеруємо унікальний ID кожної одиниці
            item_id = next(unique_id_generator)
            tech_data[item_id] = {'model': model, 'category': category, 'brand': brand, 'price': price}

            # Оновлення індексу категорії
            if category in category_index:
                category_index[category].append(item_id)
            else:
                category_index[category] = [item_id]

            # Оновлення індексу бренду
            if brand in brand_index:
                brand_index[brand].append(item_id)
            else:
                brand_index[brand] = [item_id]

    return tech_data, category_index, brand_index


def print_brand_category_statistics(tech_data, category_index, brand_index):
    print("Статистика брендів:")
    for brand, items in brand_index.items():
        print(f"{brand}: {len(items)} items")

    print("\nСтатистика категорії:")
    for category, items in category_index.items():
        print(f"{category}: {len(items)} items")


def print_items_by_brand_category(tech_data, category_index, brand_index, selected_category, selected_brand):
    print(f"\nБренд: {selected_brand} | Категорія: {selected_category}")
    for item_id in category_index[selected_category]:
        item = tech_data[item_id]
        if item['brand'] == selected_brand:
            print(f"ID: {item_id}, Model: {item['model']}, Price: {item['price']}")


def calculate_brand_distribution_by_category(tech_data, category_index, brand_index):
    brand_distribution = {}

    for category, items in category_index.items():
        brand_distribution[category] = {}
        for item_id in items:
            brand = tech_data[item_id]['brand']
            if brand in brand_distribution[category]:
                brand_distribution[category][brand] += 1
            else:
                brand_distribution[category][brand] = 1

    return brand_distribution


def print_brand_distribution(brand_distribution):
    print("\nРозподіл продукції за категоріями:")
    for category, brands in brand_distribution.items():
        print(category)
        for brand, count in brands.items():
            print(f"{brand}: {count} items")
        print()


if __name__ == '__main__':
    # Запуск програми
    file_path = 'tech_inventory.csv'
    tech_data, category_index, brand_index = read_tech_inventory(file_path)

    # Виводимо список брендів
    print("Доступні бренди:")
    for brand in brand_index.keys():
        print(brand)

    # Виводимо список категорій
    print("\nДоступні категорії:")
    for category in category_index.keys():
        print(category)

    while True:
        print("\nКоманди:")
        print("1. Натисніть 1 для виводу статистики")
        print("2. Натисніть 2 для вибіркового виводу повної інформації товару по бренду та категорії")
        print("3. Натисьніть 3 для розподілу товарів по брендам для кожної категорії")
        print("4. Натисьніть 4 для виходу")
        choice = input("Введіть номер команди для продовження: ")

        if choice == '1':
            print_brand_category_statistics(tech_data, category_index, brand_index)
        elif choice == '2':
            selected_category = input("Введіть назву категорії з урахуванням регістру: ")
            selected_brand = input("Введіть назву бренду з урахуванням регістру: ")
            print_items_by_brand_category(tech_data, category_index, brand_index, selected_category, selected_brand)
        elif choice == '3':
            brand_distribution = calculate_brand_distribution_by_category(tech_data, category_index, brand_index)
            print_brand_distribution(brand_distribution)
        elif choice == '4':
            break
        else:
            print("Помилка, спробуйте знов.")
