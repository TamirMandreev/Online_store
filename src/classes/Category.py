# -*- coding: utf-8 -*-
# Здесь описывается класс Category
from src.classes.Product import Product


# Создать класс Category.
class Category:

    # Создать атрибуты класса.
    name = str
    description = str
    __products = list

    number_of_categories = 0 # Общее количество категорий.
    number_of_different_products = 0 # Общее количество уникальных продуктов, не учитывая количество в наличии.

    # Создать конструктор класса.
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_different_products += len(products)

    # Создать строковое представление объекта.
    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    # Создать метод __len__, которые возвращает общее
    # количество продуктов категории в шт.
    def __len__(self):
        # Создать переменную счетчик.
        quantity = 0
        # Пройтись по каждому продукту из списка продуктов.
        for object in self.__products:
            # Прибавить к счетчику количество отдельно взятого продукта в шт.
            quantity += object.quantity
        # Возвратить общее количество продуктов категории в шт.
        return quantity

    # Создать метод __iter__ и __next__. Позволить объекту быть итерируемым.
    # При каждой итерации возвращает объект из списка продуктов __products.
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.__products):
            product = self.__products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

    # Создать геттер для приватного атрибута __products.
    @property
    def products(self):
        '''
        Метод products возвращает список выводов в формате
        'Продукт, 80 руб. Остаток: 15 шт.'
        :return: conclusion list
        '''
        # Создать список, куда будем складывать строки вывода
        # в формате 'Продукт, 80 руб. Остаток: 15 шт.'
        conclusion = []
        # Пройтись по каждому экземпляру класса Product,
        # которые лежат в атрибуте __products класса Category.
        for obj in self.__products:
            # Присвоить переменным product_name, price, и quantity
            # значения атрибутов экземлпяра класса Product.
            product_name = obj.name
            price = obj.price
            quantity = obj.quantity
            # Сформировать вывод.
            result = f'{product_name}, {price} руб. Остаток: {quantity} шт.'
            # Добавить вывод в список
            conclusion.append(result)

        return conclusion


    def add_product(self, product_obj):
        '''
        Метод add_product принимает на вход объект класса Product
        и добавляет его в переменную __products класса Category.
        :param product_obj: class 'src.classes.Product.Product'
        :return:
        '''
        # Проверить, является ли добавляемый продукт экземпляром
        # класса Product или его наследником.
        if isinstance(product_obj, Product):
            # Если является, добавить в список продуктов.
            self.__products.append(product_obj)
        else:
            # Если не является, вызвать исключение.
            raise TypeError

    def get_names(self):
        return self.__products
        # names = []
        # for obj in self.__products:
        #     names.append(obj.name)
        #
        # return names

