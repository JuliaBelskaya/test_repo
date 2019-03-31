# # animal_list = ['cat', 'dog']
# # for animal in animal_list:
# #     print(animal)
#
# # a_list = [23, 42]
# # for elem in a_list:
# #     print(elem)
#
# # Создать квадратную матрицу размерностью 5 и заполнить ее
# # случайными значениями. Найти сумму всех элементов матрицы,
# # которые кратны 3.
#
# from random import randint
# matrix = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(randint(1, 9))
#     matrix.append(row)
#
# for i in range(5):
#     print(matrix[i])
#
# sum = 0
# for row in matrix:
#     for elem in row:
#         if not elem % 3:
#             sum += elem
# print(sum)

# from random import randint
# n = int(input('--->'))
# m = int(input('---->'))
# matrix = []
# count = 0
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(randint(1, 9))
#     matrix.append(row)
#
# for i in range(n):
#     print(matrix[i])
#
# for row in matrix:
#     for elem in row:
#         if elem == 7:
#             count +=1
# print(count)



# from random import randint
# n = int(input('--->'))
# m = int(input('---->'))
# matrix = []
# count = 0
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(randint(1, 9))
#     matrix.append(row)
#
# for i in range(n):
#     print(matrix[i])
#
# summ = 0
# for row in matrix:
#     for elem in row:
#         summ += elem
# average = summ / (n * m)
# print(average)
#
# count = 0
# for i, row in enumerate(matrix):
#     for j, elem in enumerate(row):
#         if elem > average and not (i + j) % 2:  #не False, значит True
#             print(elem)
#             count +=1
# print(count)

# list_a = ['Петров', 'Петрова', 'Сидорова', 'Пупкина', 'Муркина']
# for i in list_a:
#     if i[0] == 'П' and i[-1] == 'а':
#         print(i)


pupils = [
  {
        'firstname': 'Masha',
        'group': 'Ivanova',
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
  {
        'firstname': 'Natasha',
        'group': 'Petrova',
        'physics': 9,
        'informatics': 7,
        'history': 6,
  },
  {
        'firstname': 'Victor',
        'group': 'Ivanov',
        'physics': 2,
        'informatics': 4,
        'history': 3,
  },
]

for pupil in pupils:
    average = (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3
    if average > 4:

        for key, value in pupil.items():
            print(f'{key}: {value}')
        print('****')