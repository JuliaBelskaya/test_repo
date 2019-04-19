animal_list = ['cat', 'dog']
for animal in animal_list:
    print(animal)

a_list = [23, 42]
for elem in a_list:
    print(elem)

    
# Создать список с фамилиями. Вывести все фамилии, 
# которые начинаются на П и заканчиваются на а

lastnames = ['Петрова', 'Иванов', 'Пирова']

for lastname in lastnames:
    if lastname[0] == 'П' and lastname[-1] == 'а':
        print(lastname)

# Создать список учеников подобной структуры. 
# Определить средний балл оценок по всем предметам, 
# и вывести сведения о студентах, средний балл которых больше 4. [02-7.3-BL-02]

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

        
# Дан двухмерный массив n × m элементов. 
# Определить, сколько раз встречается 
# число 7 среди элементов массива.[02-4.2-BL12]

from random import randint

n = int(input('n: '))
m = int(input('m: '))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(0, 9))
    matrix.append(row)

counter = 0


for row in matrix:
    print(row)
    for elem in row:
        if elem == 7:
            counter += 1
print(counter)


# Дана целочисленная матрица А[n,m]. 
# Посчитать количество элементов матрицы,
# превосходящих среднее арифметическое значение 
# элементов матрицы и сумма индексов которых четна.[02-4.2-BL23]

from random import randint

n = int(input('n: '))
m = int(input('m: '))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(0, 9))
    matrix.append(row)

summ = 0
for row in matrix:
    for elem in row:
        summ += elem

mean = summ / (n * m)
print(mean)

counter = 0
for i, row in enumerate(matrix):
    print(row)
    for j, elem in enumerate(row):
        if elem > mean and not (i + j) % 2:
            counter += 1
print(counter)
