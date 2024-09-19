import pytest
from src.classes.LawnGrass import LawnGrass

# Создать фикстуру, которая генерирует создание
# экземпляра класса LawnGrass.

@pytest.fixture
def lawn_grass_1():
    lawn_grass = LawnGrass('Засухоустойчивый',
                           'Cмесь газонных трав, состоящая из медленнорастущих сортов, не требующих частой стрижки и тщательного ухода. Используется для создания газонов с мягким покрытием в парках, вокруг загородных домов, для создания детских игровых площадок.',
                           37_400,
                           100,
                           'Light green',
                           'Дания',
                           20)
    return lawn_grass


# Тестируем создание экземпляра класса LawnGrass.
def test_LawnGrass(lawn_grass_1):
    assert lawn_grass_1.name  == 'Засухоустойчивый'
    assert lawn_grass_1.description  == 'Cмесь газонных трав, состоящая из медленнорастущих сортов, не требующих частой стрижки и тщательного ухода. Используется для создания газонов с мягким покрытием в парках, вокруг загородных домов, для создания детских игровых площадок.'
    assert lawn_grass_1.price  == 37_400
    assert lawn_grass_1.quantity  == 100
    assert lawn_grass_1.color  == 'Light green'
    assert lawn_grass_1.country_of_origin  == 'Дания'
    assert lawn_grass_1.growth_time  == 20