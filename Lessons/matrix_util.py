from random import randint


def creat(n, random_from=1, random_to=9):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(random_from, random_to))
        matrix.append(row)
    return matrix


def print_m(matrix):
    for row in matrix:
        print(row)


def summ_matrix(elem):
    summ = 0
    for row in matrix_a:
        for elem in row:
            summ += elem
    return summ


def max_matrix(matrix_a):
    max_elem = matrix_a[0][0]
    for row in matrix_a:
        for elem in row:
            if max_elem < elem:
                max_elem = elem
    return max_elem


def min_matrix(matrix_a):
    min_elem = matrix_a[0][0]
    for row in matrix_a:
        for elem in row:
            if min_elem > elem:
                min_elem = elem
    return min_elem



