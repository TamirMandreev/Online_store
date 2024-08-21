# -*- coding: utf-8 -*-
# Здесь описывается класс Category

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
        Метод add_products принимает на вход объект класса Product
        и добавляет его в переменную __products класса Category.
        :param product_obj: class 'src.classes.Product.Product'
        :return:
        '''

        self.__products.append(product_obj)

    def get_names(self):
        return self.__products
        # names = []
        # for obj in self.__products:
        #     names.append(obj.name)
        #
        # return names

