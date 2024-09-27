# -*- coding: utf-8 -*-
from src.classes.Product import Product


# Здесь описывается класс Smartphone.
class Smartphone(Product):

    # Создать аннотации типов для атрибутов класса.
    perfomance: int # Производительность.
    model: str # Модель.
    built_in_memory: int # Встроенная память.

    # Создать конструктор класса.
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, color: str, perfomance: int, model: str,
                 built_in_memory: int) -> None:
        super().__init__(name, description, price, quantity, color)
        self.perfomance = perfomance
        self.model = model
        self.built_in_memory = built_in_memory

        # Вызвать метод __repr__, чтобы при создании
        # экземпляра класса выводилось сообщение о его создании.
        # Работа данного метода определяется в классе MixinLog.
        print(self.__repr__())



