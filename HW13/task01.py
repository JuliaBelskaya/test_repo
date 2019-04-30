# Создать статичный метод get_random_name в классе Pet.
# Метод возвращает случайную строку вида A-42.

from random import (
    randint,
    choice,
)


class Pet:
    @staticmethod
    def get_random_name():
        return f'{choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}-{randint(0, 9)}{randint(0, 9)}'


print(Pet.get_random_name())