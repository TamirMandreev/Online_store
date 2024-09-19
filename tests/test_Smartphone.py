import pytest
from src.classes.Smartphone import Smartphone

# Создать фикстуру, которая генерирует создание
# экземпляра класса Smartphone.
@pytest.fixture
def smartphone_1():
    smartphone = Smartphone('Realme',
                              'Мощный процессор. Технологии Ai.\n'
                              'Snapdragon 8s | Камера Sony с ИИ ночной съемкой. \n'
                              'Самый яркий в мире флагманский дисплей.',
                              69_999,
                              100,
                              'black',
                              1650000,
                              'GT6',
                              512)
    return smartphone

# Тестируем создание экземпляра класса Smartphone.
def test_Smartphone(smartphone_1):
    assert smartphone_1.name == 'Realme'
    assert smartphone_1.description == ('Мощный процессор. Технологии Ai.\n'
                                        'Snapdragon 8s | Камера Sony с ИИ ночной съемкой. \n'
                                        'Самый яркий в мире флагманский дисплей.')
    assert smartphone_1.price == 69_999
    assert smartphone_1.quantity == 100
    assert smartphone_1.color == 'black'
    assert smartphone_1.perfomance == 1650000
    assert smartphone_1.model == 'GT6'
    assert smartphone_1.built_in_memory == 512
