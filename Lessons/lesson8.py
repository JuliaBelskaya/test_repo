# 7.4 Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1),
# random_to(по-умолчанию(9)).

# import matrix_util
#
# print(matrix_util.creat(9, 8, 9))
#


# 7.5 Создать функцию, принимающая на вход
# неопределнное количество аргументов
# и возвращающая сумму args[i]*i

# def func(*args):
#     summ = 0
#
#     for i in range(0, len(args)):
#         summ += args[i] * i
#     return summ
#
#
# print(func(4, 3, 2, 1))


# Сбор аргументов в коллекцию

# def func(*args):
#     return args
#
#
# arguments = [1, 2, 3, 4]
# print(func(arguments))  # на выходе один аргумент
# print()
# print(func(*arguments))  # распаковывает список и получается несколько значений


# Возврат функций нескольких значений


# def func(a, b):
#     summ = a + b
#     diff = a - b
#     return summ, diff
#
#
# print(func(7, 9))


# 7.6 Создать функцию, которая
# принимает на вход неопределенное
# количество аргументов и возвращает
# их сумму и максимальное из них

#
# def func(*args):
#     summ = sum(args)
#     maxi = max(args)
#     return summ, maxi
#
# print(func(4, 6, 9))


# Сбор аргументов в словарь

# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# my_func(a=5)

# 7.7 Создать функцию, которая
# принимает на вход неопределенное
# количество именных аргументов
# и выводит на экран те из них,
# длина ключа которых четна


def func(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(key, value)


func(mama=65, dad=45, sister=654)
