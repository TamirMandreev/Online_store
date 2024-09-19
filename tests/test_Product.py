import pytest
from unittest.mock import patch

from src.classes.Category import Category
from src.classes.LawnGrass import LawnGrass
from src.classes.Product import Product
from src.classes.Smartphone import Smartphone


@pytest.fixture
def product_1():
    name = 'Iphone 15'
    description = '512GB, Gray space'
    price = 210000.0
    quantity = 8
    color = 'Black'

    return Product(name, description, price, quantity, color)

@pytest.fixture
def products_list():
    return [Product('Huawei MateBook', 'Рассчитан на решение всевозможных домашних, учебных или офисных задач', 57_999,10, 'Black'),
            Product('DEXP Aquilon', 'Недорогой ПК для базовых задач', 27_999, 15, 'Black'),
            Product('MSI Katana', 'Создан для погружения в захватывающий виртуальный мир', 111_998, 20, 'Black')]

@pytest.fixture
def smartphone_1():
    smartphone_1 = Smartphone('Realme',
                              'Мощный процессор. Технологии Ai.\n'
                              ' Snapdragon 8s | Камера Sony с ИИ ночной съемкой. \n'
                              'Самый яркий в мире флагманский дисплей.',
                              69_999,
                              100,
                              'black',
                              1650000,
                              'GT6',
                              512)
    return smartphone_1

@pytest.fixture
def smartphone_2():
    smartphone_2 = Smartphone('Realme',
                              'Передовая производительность\n'
                              'Snapdragon 7+ Gen 3 / Сверхъяркий дисплей 6000 нит.',
                              59_999,
                              100,
                              'black',
                              1650000,
                              'GT 6T',
                              256)
    return smartphone_2

@pytest.fixture
def lawn_grass_1():
    lawn_grass_1 = LawnGrass('Засухоустойчивый',
                             'Cмесь газонных трав, состоящая из медленнорастущих сортов, не требующих частой стрижки и тщательного ухода. Используется для создания газонов с мягким покрытием в парках, вокруг загородных домов, для создания детских игровых площадок.',
                             37_400,
                             100,
                             'Light green',
                             'Дания',
                             20)
    return lawn_grass_1

@pytest.fixture
def lawn_grass_2():
    lawn_grass_2 = LawnGrass('Цветущий',
                             'Смесь семян газонных трав и полевых цветов, предназначенная для создания газона в виде цветущего луга. В Состав входит около 20 - ти видов однолетних и многолетних полевых цветов, отличающихся различными сроками цветения.',
                             40_000,
                             100,
                             'Light green',
                             'Дания',
                             20)
    return lawn_grass_2

# Тестируем создание экземпляра класса Product.
def test_Product(product_1):
    # Тестируем атрибуты класса Category.
    assert product_1.name == 'Iphone 15'
    assert product_1.description == '512GB, Gray space'
    assert product_1.price == 210000.0
    assert product_1.quantity == 8
    assert product_1.color == 'Black'

# Тестируем класс-метод create_product. Ситуация, когда
# создаваемый продукт уже существует. При этом новая цена больше старой.
def test_create_product_existing_price_increase(products_list):
    # Имитируем ввод с клавиатуры.
    with patch('builtins.input', side_effect=['Huawei MateBook', 100000, 10]):
        product = Product.create_product(products_list)

    # Проверяем, что продукт создан с правильными атрибутами.
    assert product.name == 'Huawei MateBook'
    assert product.description == 'Рассчитан на решение всевозможных домашних, учебных или офисных задач'
    assert product.price == 100000
    assert product.quantity == 20
    assert product.color == 'Black'

# Тестируем класс-метод create_product. Ситуация, когда
# создаваемый продукт уже существует. При этом новая цена меньше старой.
def test_create_product_existing_price_reduction(products_list):
    # Имитируем ввод с клавиатуры.
    with patch('builtins.input', side_effect=['Huawei MateBook', 10, 10]):
        product = Product.create_product(products_list)

    # Проверяем, что продукт создан с правильными атрибутами.
    assert product.name == 'Huawei MateBook'
    assert product.description == 'Рассчитан на решение всевозможных домашних, учебных или офисных задач'
    assert product.price == 57_999
    assert product.quantity == 20

# Тестируем класс-метод create_product. Ситуация, когда
# создаваемый продукт новый.
def test_create_product_new(products_list):
    # Имитируем ввод с клавиатуры.
    # Цвет товара остается старымж
    # Цвет товара остается старымж
    with patch('builtins.input', side_effect=['Новый продукт', 'С помощью этого описания мы тестируем метод create_product', 25.5, 5, 'Black']):
        product = Product.create_product(products_list)

    # Проверяем, что продукт создан с правильными атрибутами.
    assert product.name == 'Новый продукт'
    assert product.description == 'С помощью этого описания мы тестируем метод create_product'
    assert product.price == 25.5
    assert product.quantity == 5
    assert product.color == 'Black'

# Тестируем геттер атрибута price
def test_getter_price(product_1):
    assert product_1.price == 210_000

# Тестируем сеттер атрибута price. Ситуация, когда
# новая цена выше старой.
def test_setter_price_valid(product_1):
    product_1.price = 500_000
    assert product_1.price == 500_000

# Тестируем сеттер атрибута price. Ситуация, когда
# новая цена ниже старой. И пользователь соглашается ее изменить.
def test_setter_price_lower_than_current_price_yes(product_1):
    with patch('builtins.input', side_effect=['д']):
        product_1.price = 10
        assert product_1.price == 10

# Тестируем сеттер атрибута price. Ситуация, когда
# новая цена ниже старой. Но пользователь отказывается ее менять.
def test_setter_price_lower_than_current_price_no(product_1):
    with patch('builtins.input', side_effect=['н']):
        product_1.price = 10
        assert product_1.price == 210_000

# Тестируем сеттер атрибута price. Ситуация, когда
# новая цена указана неправильно (Если цена меньше или равна нулю).
def test_setter_price_incorrect(product_1):
    with patch('builtins.print') as mock_print:
        product_1.price = -100
        mock_print.assert_called_once_with('Цена введена некорректно.')
        assert product_1.price == 210_000

# Тестируем метод __str__.
def test_str(product_1):
    assert product_1.__str__() == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'

# Тестируем метод __add__.
def test_add(products_list, smartphone_1, smartphone_2,
             lawn_grass_1, lawn_grass_2):
    # Ситуация, когда экземпляры класса принадлежат классу Product.
    assert products_list[0] + products_list[1] == 999975
    # Ситуация, когда экземпляры класса принадлежат
    # дочернему классу Smartphone.
    assert smartphone_1 + smartphone_2 == 12999800
    assert lawn_grass_1 + lawn_grass_2 == 7740000
    # Ситуация, когда складываемые экземпляры принадлежат
    # разным классам.
    with pytest.raises(TypeError):
        lawn_grass_1 + smartphone_1






