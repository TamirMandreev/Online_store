import json
from pprint import pprint
from src.classes.Category import Category


def load_categories_from_json(file_path):
    ''' Функция load_categories_from_json загружает данные
    из json файла и на их основе создает список экземпляров
    класса Category.
    Принимает на вход путь к файлу в виде строки, возвращает
    список экземпляров класса Category.
    :param file_path str
    :return categories list'''

    # Создать пустой списк. В него будем сохранять
    # экземпляры класса Category.
    categories = []

    # Открыть json файл в режиме чтения.
    with open(file_path, 'r') as file:
        # Загрузить данные файла в переменную data.
        data = json.load(file)

    # Пройтись по каждому словарю из списка словарей data.
    for item in data:
        # Сохранить значения ключей name, description и __products
        # в соответствующие переменные.
        name = item.get('name')
        description = item.get('description')
        products = item.get('__products')

        # Создать на основе данных экземпляр класса Category.
        category = Category(name, description, products)
        # Добавить в переменную categories созданный экземпляр.
        categories.append(category)

    # Вернуть список полученных экземпляров.
    return categories

load_categories_from_json('../src/products.json')