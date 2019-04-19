# 7.1 Написать функцию, которая получает
# на вход имя и выводит строку вида:
# “Hello, {name}”. Создать список
# из 5 имен. Вызвать функцию
# для каждого элемента списка в цикле.
#
def a(name):
    print(f'Hello, {name}')

List_a = ['ff', 'ffs', 'gsv', 'dsaf', 'fdfd']
for name in List_a:
    a(name)

# 7.2 Написать программу для нахождения факториала.
# Факториал натурального числа n определяется
# как произведение всех натуральных чисел
# от 1 до n включительно
#
def fuct(n):
    mult = 1
    for i in range(1, n+1):
        mult *= i
    return mult
print(fuct(5))

#var2

def factorial(n):
    i = n
    result = 1
    while i:
        result *= i
        i -= 1
    return result

print(factorial(4))

# 7.3 Написать программу для работы
# с матрицами: создание, вывод,
# сумма всех элементов, нахождение
# максимального, минимального элемента.


from random import randint


def creat(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(1, 10))
        matrix.append(row)
    return matrix


def print_m(matrix):
    for row in matrix:
        print(row)


matrix_a = creat(5)
print_m(matrix_a)


def summ_matrix(elem):
    summ = 0
    for row in matrix_a:
        for elem in row:
            summ += elem
    return summ


s = summ_matrix(5)
print(s)


def max_matrix(matrix_a):
    max_elem = matrix_a[0][0]
    for row in matrix_a:
        for elem in row:
            if max_elem < elem:
                max_elem = elem
    return max_elem


b = max_matrix(matrix_a)
print(b)


def min_matrix(matrix_a):
    min_elem = matrix_a[0][0]
    for row in matrix_a:
        for elem in row:
            if min_elem > elem:
                min_elem = elem
    return min_elem


c = min_matrix(matrix_a)
print(c)


#var2
from random import randint


def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(1, 9))
        matrix.append(row)
    return matrix

a = create_matrix(5)
print(a)
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

def sum_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in matrix:
            summ += elem
    return summ

def get_max_elem(matrix):
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem

def get_min_elem(matrix):
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem


matrix_a = create_matrix(5)
print_matrix(matrix_a)
print(get_max_elem(matrix_a))
print(get_min_elem(matrix_a))
