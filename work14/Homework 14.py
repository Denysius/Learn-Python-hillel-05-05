import os
import csv
import json
from datetime import datetime


class Event:
    def __init__(self, data):
        self.data = data

    def process(self):
        # Визначаємо тип операції та обробляємо відповідно до нього
        operation_type = self.data['operation']
        if operation_type == 'first_arrival':
            self.process_first_arrival()
        elif operation_type == 'sale':
            self.process_sale()
        elif operation_type == 'move':
            self.process_move()
        elif operation_type == 'dispose':
            self.process_dispose()
        else:
            print(f"Невідомий тип операції: {operation_type}")

    def process_first_arrival(self):
        # Обробляємо перше прибуття SKU на склад
        print("Обробка першого прибуття:")
        print(self.data)

    def process_sale(self):
        # Обробляємо продаж SKU клієнту
        print("Обробка продажу:")
        print(self.data)

    def process_move(self):
        # Обробляємо перевезення SKU на новий склад
        print("Обробка перевезення:")
        print(self.data)

    def process_dispose(self):
        # Обробляємо утилізацію товару що просрочено
        print("Обробка утилізації:")
        print(self.data)


class DataEntry:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.data_list = []

    def read_files_from_directory(self):
        # Зчитуємо файли з заданого каталогу
        file_paths = [os.path.join(self.directory_path, filename) for filename in os.listdir(self.directory_path)]
        for file_path in file_paths:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.parse_file_content(content)

    def parse_file_content(self, content):
        # Розпізнаємо формат даних (JSON або CSV) і зберігаємо їх у списку
        try:
            data = json.loads(content)
            if isinstance(data, list):
                self.data_list.extend(data)
                return
        except json.JSONDecodeError:
            pass

        try:
            csv_reader = csv.DictReader(content.splitlines())
            for row in csv_reader:
                self.data_list.append(row)
        except csv.Error:
            pass

    def process_data(self):
        # Обробляємо всі дані в списку
        for data in self.data_list:
            event = Event(data)
            event.process()


class Metrics:
    def __init__(self, data_list):
        self.data_list = data_list

    def calculate_profit_from_sales(self):
        # Розраховуємо прибуток від продажу
        profit = sum(float(row['operation_cost']) for row in self.data_list if row['operation'] == 'sale')
        formatted_profit = '{:.2f}'.format(profit)
        return formatted_profit

    def calculate_lost_skus(self, current_date):
        lost_skus = 0
        for row in self.data_list:
            if row['operation'] == 'sale' and row['expiration_date']:
                expiration_date = datetime.strptime(row['expiration_date'], '%Y-%m-%d')
                if expiration_date < current_date:
                    lost_skus += 1
        return lost_skus

    def calculate_products_through_warehouses(self):
        # Розраховуємо кількість продуктів, що проходять через кожен склад
        products_through_warehouses = {}
        for row in self.data_list:
            warehouse = row['warehouse']
            if warehouse not in products_through_warehouses:
                products_through_warehouses[warehouse] = 0
            products_through_warehouses[warehouse] += 1
        return products_through_warehouses

    def calculate_products_sold_by_warehouse(self):
        # Розраховуємо кількість продуктів, проданих з кожного складу
        products_sold_by_warehouse = {}
        for row in self.data_list:
            if row['operation'] == 'sale':
                warehouse = row['warehouse']
                if warehouse not in products_sold_by_warehouse:
                    products_sold_by_warehouse[warehouse] = 0
                products_sold_by_warehouse[warehouse] += 1
        return products_sold_by_warehouse

    def calculate_products_disposed_by_warehouse(self):
        # Розраховуємо кількість продуктів, утилізованих з кожного складу
        products_disposed_by_warehouse = {}
        for row in self.data_list:
            if row['operation'] == 'dispose':
                warehouse = row['warehouse']
                if warehouse not in products_disposed_by_warehouse:
                    products_disposed_by_warehouse[warehouse] = 0
                products_disposed_by_warehouse[warehouse] += 1
        return products_disposed_by_warehouse

    def calculate_all_data_by_sku_index(self):
        # Виводимо всі дані, відсортовані за індексом SKU
        indexer = Indexer(self.data_list)
        print("Всі дані, відсортовані за індексом SKU:")
        for sku, rows in sorted(indexer.sku_index.items()):
            print(f"SKU: {sku}")
            for row in rows:
                print(row)

    def calculate_all_data_by_warehouse_index(self):
        # Виводимо всі дані, відсортовані за індексом складу
        indexer = Indexer(self.data_list)
        print("Всі дані, відсортовані за індексом складу:")
        for warehouse, rows in sorted(indexer.warehouse_index.items()):
            print(f"Склад: {warehouse}")
            for row in rows:
                print(row)

    def calculate_all_data_by_operation_index(self):
        # Виводимо всі дані, відсортовані за індексом операції
        indexer = Indexer(self.data_list)
        print("Всі дані, відсортовані за індексом операції:")
        for operation, rows in sorted(indexer.operation_index.items()):
            print(f"Операція: {operation}")
            for row in rows:
                print(row)


class Indexer:
    def __init__(self, data_list):
        self.data_list = data_list
        self.sku_index = {}
        self.warehouse_index = {}
        self.operation_index = {}
        self.create_indexes()

    def create_indexes(self):
        # Створюємо індекси для SKU, складів і операцій
        for row in self.data_list:
            sku = row['sku']
            warehouse = row['warehouse']
            operation = row['operation']

            if sku not in self.sku_index:
                self.sku_index[sku] = []
            self.sku_index[sku].append(row)

            if warehouse not in self.warehouse_index:
                self.warehouse_index[warehouse] = []
            self.warehouse_index[warehouse].append(row)

            if operation not in self.operation_index:
                self.operation_index[operation] = []
            self.operation_index[operation].append(row)


if __name__ == '__main__':
    directory_path = r'C:\Users\Денис\PycharmProjects\Learn-Python-hillel-05-05\work14\SKU'
    data_processor = DataEntry(directory_path)
    data_processor.read_files_from_directory()
    data_processor.process_data()

    metrics = Metrics(data_processor.data_list)

    print("Доступні метрики:")
    print("1. Прибуток від продажу")
    print("2. Кількість втрачених SKU (wait for update)")
    print("3. Кількість продуктів, що проходять через кожен склад")
    print("4. Кількість продуктів, проданих з кожного складу")
    print("5. Кількість продуктів, утилізованих з кожного складу")
    print("6. Всі дані, відсортовані за індексом SKU")
    print("7. Всі дані, відсортовані за індексом складу")
    print("8. Всі дані, відсортовані за індексом операції")

    while True:
        try:
            choice = int(input("Введіть номер метрики, яку ви хочете розрахувати (або 0 для виходу): "))
            if choice == 1:
                profit_from_sales = metrics.calculate_profit_from_sales()
                print(f"Прибуток від усіх операцій продажу: {profit_from_sales}")
            elif choice == 2:
                date_str = input("Введіть поточну дату (у форматі 'рік-місяць-день'): ")
                current_date = datetime.strptime(date_str, '%Y-%m-%d')
                lost_skus = metrics.calculate_lost_skus(current_date)
                print(f"Кількість унікальних SKU, які не були продані на дату {current_date}: {lost_skus}")
            elif choice == 3:
                products_through_warehouses = metrics.calculate_products_through_warehouses()
                print("Кількість продуктів, що проходять через кожен склад:")
                print(products_through_warehouses)
            elif choice == 4:
                products_sold_by_warehouse = metrics.calculate_products_sold_by_warehouse()
                print("Кількість продуктів, проданих з кожного складу:")
                print(products_sold_by_warehouse)
            elif choice == 5:
                products_disposed_by_warehouse = metrics.calculate_products_disposed_by_warehouse()
                print("Кількість продуктів, утилізованих з кожного складу:")
                print(products_disposed_by_warehouse)
            elif choice == 6:
                metrics.calculate_all_data_by_sku_index()
            elif choice == 7:
                metrics.calculate_all_data_by_warehouse_index()
            elif choice == 8:
                metrics.calculate_all_data_by_operation_index()
            elif choice == 0:
                print("Завершення програми.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Некоректне введення. Введіть число.")
