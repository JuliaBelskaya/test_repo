# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и
# сохранить в другой файл [my-files-t01]

import json
from random import randint


def create_matrix(n):
    matrix = [[randint(1,9) for j in range(n)] for i in range(n)]
    return matrix

def write_matrix_to_file(matrix, filename='files/matrix.json'):
    with open(filename, 'w') as matrix_file:
        data = json.dumps(matrix)
        matrix_file.write(data)

def read_json_file(filename='files/matrix.json'):
    with open(filename) as matrix_file:
        matrix = json.loads(matrix_file.read())
    return matrix

def make_zero_even_matrix(matrix):
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if not elem % 2:
                matrix[i][j] = 0

def main():
    matrix = create_matrix(5)
    write_matrix_to_file(matrix)
    read_matrix = read_json_file()
    make_zero_even_matrix(matrix)
    write_matrix_to_file(matrix, 'files/new_matrix.json')

if __name__ == "__main__":
    main()
