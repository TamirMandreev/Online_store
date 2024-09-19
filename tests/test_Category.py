import pytest
from src.classes.Category import Category
from src.classes.Product import Product
from tests.test_Product import product_1


# Фикстура create_products создает экземпляры класса Product - ноутбуки.
@pytest.fixture
def create_products_laptops():
    product_1 = Product('Huawei MateBook', 'Рассчитан на решение всевозможных домашних, учебных или офисных задач', 57_999, 10, 'black')
    product_2 = Product('DEXP Aquilon', 'Недорогой ПК для базовых задач', 27_999, 15, 'black')
    product_3 = Product('MSI Katana', 'Создан для погружения в захватывающий виртуальный мир', 111_998, 20, 'black')
    return [product_1, product_2, product_3]


# Фикстура create_products создает экземпляры класса Product - смартфоны.
@pytest.fixture
def create_products_smartphones():
    product_1 = Product('Apple iPhone 15', 'Непревзойденное сочетание цвета и долговечности', 81_899, 15, 'black')
    product_2 = Product('Samsung Galaxy A 55', 'Сохраняет яркость и четкость изображений при любом освещении', 43_999, 25, 'black')
    product_3 = Product('Realme Note 50', 'Бюджетный смартфон для тех, кто старается быть продуктивным', 7_499, 40, 'black')
    return [product_1, product_2, product_3]


# Фикстура category_1 создает экземпляр класса Category - ноутбуки.
@pytest.fixture
def category_1(create_products_laptops):
    name = 'Ноутбуки'
    description = ('Ноутбуки как незаменимый инструмент дома и на работе.')
    products = create_products_laptops


    return Category(name, description, products)

# Фикстура category_2 создает экземпляр класса Category - смартфоны.
@pytest.fixture
def category_2(create_products_smartphones):
    name = 'Смартфоны'
    description = ('Смартфоны - неотъемлемая часть нашей жизни')
    products = create_products_smartphones

    return Category(name, description, products)

@pytest.fixture
def random_obj():
    class Random_obj:
        pass
    return Random_obj


def test_Category(category_1, category_2):
    # Тестируем атрибуты класса Category.
    assert category_1.name == 'Ноутбуки'
    assert category_1.description == ('Ноутбуки как незаменимый инструмент дома и на работе.')
    assert Category.number_of_categories == 2
    assert Category.number_of_different_products == 6

    # Тестируем атрибут __products. Отдельно, потому что он
    # возвращает из списка __products описание экземпляров
    # класса Product с помощью цикла. Тестируем цикл.
    assert category_1.products[0] == 'Huawei MateBook, 57999 руб. Остаток: 10 шт.'
    assert category_1.products[1] == 'DEXP Aquilon, 27999 руб. Остаток: 15 шт.'
    assert category_1.products[2] == 'MSI Katana, 111998 руб. Остаток: 20 шт.'

# Тестируем метод __str__.
def test_str(category_1):
    assert category_1.__str__() == 'Ноутбуки, количество продуктов: 45 шт.'


# Тестируем метод add_product.
def test_add_product(category_1, product_1, random_obj):
    # Добавляем к category_1 один экземпляр класса product.
    category_1.add_product(product_1)
    # Проверяем количество продуктов. Должно быть +1.
    assert len(category_1.get_names()) == 4
    # Проверяем добавление экземпляра, которые не принадлежит
    # к классу Product или его потомкам.
    with pytest.raises(TypeError):
        category_1.add_product(random_obj)