#task_1

from random import randint
matrix = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(randint(-5, 5))
    matrix.append(row)

for i in range(5):
   print(matrix[i])


max_elem = 0
for row in matrix:
    for elem in row:
        if abs(elem) > abs(max_elem):
            max_elem = elem

new_matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(matrix[i][j] / max_elem)
    new_matrix.append(row)

print(*new_matrix, '\n', sep='\n')
