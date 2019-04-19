#Получить сумму кубов первых n натуральных чисел используя цикл while

# n = int(input('Введите число'))
# i = 1 # натуральные числа начинаются с 1
# summ = 0
# while i <= n:
#     summ += i ** 3
#     i += 1
# print(summ)

#НАписать программу которая будет выводить на экран случайные числа от 1 до 10 до тех пор пока не выпадет 7

# from random import randint
# while True:
#     n = randint(1, 10)
#     if n == 7:
#         break
#     print(n)
#
# Получить сумму кубов натуральных чисел от n до m используя цикл for

# n = int(input('Введите число '))
# m = int(input('Введите еще число '))
# summ = 0
# for i in range(n, m):
#     summ += i ** 3
# print(summ)

# Ввести два целых числа А и В (A<B)/ Вывести в порядке возрастания все целые числа,
# расположенные между А и В (включая сами числа А и В), а также количество N этих чисел

# A = int(input('Введите число '))
# B = int(input('Ввести еще одно число больше первого '))
# count = 0
# for i in range (A, B+1):
#     count += 1
#     print(i)
# print(f'amount is {count}')

#Создать квадтратную матрицу размерностью n и заполнить ее случаными значениями от 1 до 9


from random import randint

n = int(input('n: '))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(str(randint(1, 9)))
    matrix.append(row)
print(matrix)

for i in range(n):
    row = ' '.join(matrix[i])
    print(row)
    
#Найти сумму всех элементов матрицы которые кратны 3

from random import randint

n = int(input('n: '))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(1, 9))
    matrix.append(row)
print(matrix)

summ = 0
for i in range(n):
    for j in range(n):
        if not matrix[i][j] % 3:
            summ += matrix[i][j]
print(summ)


