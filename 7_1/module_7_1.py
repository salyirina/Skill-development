class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight  # общий вес товара (дробное число)
        self.category = category   # категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name):
        self.__file_name = file_name

    # Метод get_products(self), который считывает всю информацию из файла __file_name
    # и возвращает единую строку со всеми товарами из файла __file_name.
    def _read_file(self):
        try:
            file = open(self.__file_name, 'r', encoding='utf-8')
            content = file.read().strip()
            file.close()
            return content
        except FileNotFoundError:
            return ""  # Если файл не найден, возвращаем пустую строку

    # Метод для открытия файла и добавления новых данных write_to_file(запись в файл)
    def _write_to_file(self, content):
        file = open(self.__file_name, 'a', encoding='utf-8')
        file.write(content)
        file.close()

    # Метод get_products(self), который считывает всю информацию из файла __file_name
    # и возвращает единую строку со всеми товарами из файла __file_name.
    def get_products(self):
        content = self._read_file()
        if content:
            return content
        else:
            return ""

    # Метод add_product(self, *products), который принимает неограниченное количество = {} объектов класса Product
    # и добавляет их в файл __file_name, если их там ещё нет (по названию).
    def add_product(self, *products):
        """Считывает все продукты из файла и возвращает их в виде строки."""
        existing_products = set()
        content = self._read_file()
        if content:
            for line in content.split('\n'):
                existing_products.add(line.strip().split(',')[0])

        # Добавляем новые продукты в файл
        for product in products:
            if product.name not in existing_products:
                content = f'{product.name}, {product.weight}, {product.category}\n'
                self._write_to_file(content)
                existing_products.add(product.name)
            else:
                print(f'Продукт {product.name} уже есть в магазине.')


# Пример использования:
s1 = Shop("products.txt")
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add_product(p1, p2, p3)

print(s1.get_products())
