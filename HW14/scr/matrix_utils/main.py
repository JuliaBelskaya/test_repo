# Создать в файле main.py матрицу.
# Воспользоваться всеми описанными функциями и методами.

from random import randint
from scr.matrix_utils.matrix_classes import Matrix
import scr.matrix_utils.matrix_funcs as func


if __name__ == "__main__":

    data = [[randint(1, 9) for _ in range(5)] for _ in range(5)]
    matrix = Matrix(data)
    print(matrix)

    print(func.matrix_sum(data))
    print(func.matrix_max(data))
    print(func.matrix_min(data))
