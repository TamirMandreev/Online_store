# -*- coding: utf-8 -*-
# Здесь описывается класс Product.

# Создать класс Product.
class Product:

    # Создать атрибуты класса.
    name = str
    description = str
    price = float
    quantity = int

    # Создать конструктор класса.
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    # Создать строковое представление объекта.
    def __str__(self):
        return f'{self.name}, {self._price} руб. Остаток: {self.quantity} шт.'

    # Создать метод __add__, который складывает
    # price * quantity двух продуктов.
    def __add__(self, other):
        return (self._price * self.quantity) + (other._price * other.quantity)

    @classmethod
    def create_product(cls, products_list):

        # Узнать у пользователя наименование товара.
        name = input('Название товара: ')
        # Запустить цикл, который переберет все продукты из products_list.
        # products_list - это список экземпляров класса Product.
        for existing_product in products_list:
            # Сравнить имя продукта с именем нового продукта.
            if existing_product.name == name:
                # Сообщить пользователю, что данный продукт уже имеется в списке продуктов.
                print('Данный продукт уже имеется в списке продуктов.')
                # Описание товара остается старым.
                description = existing_product.description
                # Узнать у пользователя цену товара.
                price = float(input('Цена: '))
                # Если новая цена меньше старой, то оставить старую цену.
                if price < existing_product.price:
                    price = existing_product.price
                # Узнать у пользователя количество товара.
                quantity = int(input('Количество: ')) + existing_product.quantity

                # Возвратить экземпляр класса Product.
                return cls(name, description, price, quantity)

            else:
                # Узнать у пользователя описание товара.
                description = input('Описание товара: ')
                # Узнать у пользователя цену товара.
                price = float(input('Цена: '))
                # Узнать у пользователя количество товара.
                quantity = int(input('Количество: '))

                # Возвратить экземпляр класса Product.
                return cls(name, description, price, quantity)



    @property
    def price(self):
        '''
        Геттер атрибута price. Возвращает 'self._price' .
        '''
        return self._price

    @price.setter
    def price(self, price):
        '''
        Сеттер атрибута self._price.
        Если новая цена меньше или равна нулю: print('Цена введена некорректно.')
        Если новая цена меньше текущей цены: функция спрашивает пользователя: ''Вы хотите понизить цену?'. Если 'да', то цена меняется. Если 'нет', цена остается прежней.
        Во всех другий случаях изменяет цену.
        :param price:
        :return:
        '''
        if price <= 0:
            print("Цена введена некорректно.")
            return
        elif price < self._price:
            user_answer = input('Вы хотите понизить цену? д = да, все остальное = нет\n'
                                'Введите ответ: ')
            if user_answer == 'д':
                self._price = price
                print('Цена изменена.')
                return
            else:
                print("Изменение цены отменено.")
                return
        else:
            self._price = price