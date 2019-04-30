# Описать функции, которые принимают на вход объект класса Matrix.
# Функции позволяют искать максимальный элемент матрицы,
# минимальный, сумму всех элементов.

from scr.matrix_utils.matrix_classes import Matrix


def matrix_min(matrix: Matrix) -> int:
    return min(min(row) for row in matrix)


def matrix_max(matrix: Matrix) -> int:
    return max(max(row) for row in matrix)


def matrix_sum(matrix: Matrix):
    return sum(sum(row) for row in matrix)
