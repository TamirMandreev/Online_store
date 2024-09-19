# -*- coding: utf-8 -*-
from src.classes.Product import Product


# Здесь описывается класс LawnGrass.
class LawnGrass(Product):

    # Создать аннотации типов для атрибутов класса.
    country_of_origin: str # Страна производитель
    growth_time = int # Время роста

    # Создать конструктор класса.
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, color: str, country_of_origin: str,
                 growth_time: int) -> None:
        super().__init__(name, description, price, quantity, color)
        self.country_of_origin = country_of_origin
        self.growth_time = growth_time
