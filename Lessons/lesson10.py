# map()
# result = map(lambda x: x ** 2, [1,2,3,4,5,6])
# print(list(result))


# 9.7 Дан список чисел.
# Вернуть список, где каждый число переведено в строку
# [5, 3] -> [‘5’, ‘3’]


# result = map(str, [5, 3])
# print(list(result))

# new_list = []
# for elem in [1, 2, 3]
#     new_list.append(str(elem))

# filter()
# result = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])
# print(list(result))

# 9.8 Дан список имен, отфильтровать все имена, где есть буква k

# list_name = filter(lambda elem: "k" in elem or "K" in elem, ["Kate", "Pasha", "Nick"])
# print(list(list_name))

# names = ['kate', 'mark', 'nil']
# result = (filter(lambda name: 'k' in name, names))
# print(list(result))

# reduce()
# from functools import reduce
# result = reduce(lambda a, x: a + x ** 2, [1,2,3], 0)
# print(result)

# 9.9 Дан список чисел. Найти произведение всех чисел, которые кратны 3.

# 1 способ:
# from functools import reduce
# result = reduce(lambda a, x: a * x, [a for a in [2, 3, 5, 6] if a % 3 == 0], 1)
# print(result)
#
# 2 способ:
# from functools import reduce
# result = reduce(lambda a, x: a * x, filter(lambda a: a % 3 == 0, [2, 3, 5, 6]), 1)
# print(result)

# def main():
#     my_file = open('test.txt')
#     print(my_file)
#     my_file.close()
# if __name__ == '__main__':
#   main()


# def main():
#     my_file = open('test.txt')
#     print(my_file.readline().strip())
#     print(my_file.readline())
#     my_file.close()
#
# if __name__ == '__main__':
#   main()


# def main():
#     my_file = open('test.txt')
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print(line)
#     my_file.close()
#
# if __name__ == '__main__':
#   main()

# 10.1 Имеется текстовый файл. Напечатать:
# а) его первую строку;
# б) его пятую строку;
# в) его первые 5 строк;
# г) его строки с s1-й по s2-ю;
# д) весь файл.
# [03-15.16]

# a) его первую строку;
# def main():
#     my_file = open('test.txt')
#     print(my_file.readline())
#     my_file.close()
#
# if __name__ == '__main__':
#   main()

# b) его пятую строку;
# def main():
#     my_file = open('test.txt')
#     count = 1
#     while True:
#         line = my_file.readline()
#         if count == 5:
#             print(line)
#         if not line:
#             break
#         count += 1
#
#     my_file.close()
#
# if __name__ == '__main__':
#   main()


# в) его первые 5 строк;
# def main():
#     my_file = open('test.txt')
#     count = 1
#     while True:
#         line = my_file.readline().strip()
#         if count < 6:
#             print(line)
#         count += 1
#         if not line:
#             break
#     my_file.close()

# if __name__ == '__main__':
#   main()

# г) его строки с s1-й по s2-ю;
# def main():
#     my_file = open('test.txt')
#     count = 1
#     s1 = 2
#     s2 = 4
#     while True:
#         line = my_file.readline().strip()
#         if count <= s2 and count >= s1:
#             print(line)
#         count += 1
#         if not line:
#             break
#     my_file.close()
#
# if __name__ == '__main__':
#   main()


# д) весь файл.
# def main():
#     my_file = open('test.txt')
#     count = 1
#     while True:
#         line = my_file.readline().strip()
#         print(line)
#         count += 1
#         if not line:
#             break
#     my_file.close()
#
# if __name__ == '__main__':
#   main()

# Чтение всех строк файла
#
# my_file = open('test.txt')
# print(my_file.readlines())

# Открытие с помощью with
#
# with open('test.txt') as my_file:
#     for line in my_file.readlines():
#         print(line.strip())


# 10.2 Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.


def main():
    with open("test.txt", "w") as my_file:

        for lines in range(6):
            my_file.write(input("Enter 6 lines: ") + "\n")


if __name__ == "__main__":
    main()


# Построчная запись в файл
#
# with open('test.txt', 'w') as my_file:
#     my_file.write('qwerty')


# with open('test.txt', 'w') as my_file:
#    my_file.writelines(['qwerty\n', 'asdf'])
#
