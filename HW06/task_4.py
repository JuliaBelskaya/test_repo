# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]

n = int(input('->'))
s = 0
for i in range(1, n + 1):
    s += 1 / i
print(s)

#var2

n = int(input('N: '))
s = 0
for i in range(1, n + 1):
    s += 1 / i
print(f'S is {s}')
