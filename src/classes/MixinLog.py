# -*- coding: utf-8 -*-
# Здесь описывается класс MixinLog.

# Создать класс MixinLog.
class MixinLog:

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes_str = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Создан экземпляр класса {class_name} с атрибутами {attributes_str}'


