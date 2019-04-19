    
# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]

from random import randint
from itertools import groupby
 
l = [randint(1,10) for _ in range(100)]
s = ''
for i in range(1,len(l)):
    if l[i-1] < l[i]: 
        s += '+'
    else: s += '-'

g = groupby(s)
out = [k for k,v in g if k == '+']
print('result:',len(out))
        
#var2

from random import randint

n = 10
numbers = []
for i in range(n):
    numbers.append(randint(-10, 10))
print(numbers)

amount = 0
is_same = False
for i in range(1, n):
    if numbers[i] > numbers[i-1]:
        if not is_same:
            amount += 1
            is_same = True
    else:
        is_same = False

print(amount)
