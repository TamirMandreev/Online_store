# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

# Здесь описывается класс Item. Он является абстрактным.

# Создать класс Item. Унаследовать его от ABC.
class Item(ABC):

    # Создать аннотацию типов для атрибутов класса.
    name = str
    description = str
    _price = float
    quantity = int

    # Создать конструктор класса.
    @abstractmethod
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, color: str) -> None:
        pass
