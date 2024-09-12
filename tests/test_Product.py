import pytest
from unittest.mock import patch

from src.classes.Category import Category
from src.classes.Product import Product

@pytest.fixture
def product_1():
    name = 'Iphone 15'
    description = '512GB, Gray space'
    price = 210000.0
    quantity = 8

    return Product(name, description, price, quantity)

@pytest.fixture
def products_list():
    return [Product('Huawei MateBook', 'Рассчитан на решение всевозможных домашних, учебных или офисных задач', 57_999,10),
            Product('DEXP Aquilon', 'Недорогой ПК для базовых задач', 27_999, 15),
            Product('MSI Katana', 'Создан для погружения в захватывающий виртуальный мир', 111_998, 20)]



# Тестируем создание экземпляра класса Product.
def test_Product(product_1):
    # Тестируем атрибуты класса Category.
    assert product_1.name == 'Iphone 15'
    assert product_1.description == '512GB, Gray space'
    assert product_1.price == 210000.0
    assert product_1.quantity == 8

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
    with patch('builtins.input', side_effect=['Новый продукт', 'С помощью этого описания мы тестируем метод create_product', 25.5, 5]):
        product = Product.create_product(products_list)

    # Проверяем, что продукт создан с правильными атрибутами.
    assert product.name == 'Новый продукт'
    assert product.description == 'С помощью этого описания мы тестируем метод create_product'
    assert product.price == 25.5
    assert product.quantity == 5

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
def test_add(products_list):
    assert products_list[0] + products_list[1] == 999975






