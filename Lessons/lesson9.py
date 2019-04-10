# 9.1 Дан список слов.
# Сгенерировать новый список с перевернутыми словами

# list_b = ['papa', 'asd']
# list_a = [word[::-1] for word in list_b]
# print(list_a)

# 9.2 Дан список словарей.
# Каждый словарь описывает машину
# (серийный номер и год выпуска).
# Создать новый список со всеми машинами,
# год выпуска которых больше n


# n = int(input('Enter a year'))
# list_a = [
#     dict(number='01', year=1996),
#     dict(number='02', year=1999),
#     dict(number='03', year=1998),
# ]
# list_b = [car for car in list_a if car['year'] > n]     #для car в списке, если год в car больше n, возвращаем взначение car
# print(list_b)


# Создание матрицы

# from random import randint
#
# n = 3
# matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
# print(matrix)

# Генератор словарей

# old_dict = {"aa": 1, "b": 2, "cccc": 3}
# new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
# print(new_dict)

# 9.3 Дан словарь, создать новый словарь,
# поменяв местам ключ и значение

# old_dict = {"aa": 1, "b": 2, "cccc": 3}
# new_dict = {value: key for key, value in old_dict.items()}
# print(new_dict)

# 9.4 Создать lambda функцию, которая
# принимает на вход имя и выводит его в формате “Hello, {name}”

# print((lambda name: f"Hello, {name}")("Mark"))

# 9.5
#Создать lambda функцию, которая
# принимает на вход список имен
# и выводит их в формате “Hello, {name}”


# print((lambda names: [f'Hello, {name}' for name in names])(['aa', 'bb']))

# 9.6 Написать декоратор, который
# будет выводить время выполнения функции

from datetime import datetime
from time import sleep

def my_decorator(func):
    def wrapper (*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Func time is: {end - start}')
        return result
    return wrapper

@my_decorator
def sleep_func(n):
    sleep(n)
    return 'a'

print(sleep_func(2))

