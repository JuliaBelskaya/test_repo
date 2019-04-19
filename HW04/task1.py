# Дан список целых чисел. Создать новый список, каждый элемент которого 
# равен исходному элементу умноженному на -2


lst = list(range(1, 11))
new_lst = []
i = 0
while i < len(lst):
    new_lst.append(lst[i] * -2)
    i += 1
print(new_lst)

# вариант 2
numbers = [1, 5, 7, -10, -2]
mult_numbers = []
i = 0
numbers_len = len(numbers)
while i < numbers_len:
    mult_numbers.append(numbers[i] * -2)
    i += 1
print(mult_numbers)
