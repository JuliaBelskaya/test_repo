# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]

for n in range(200, 300):
    s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
    if s > n:
        result = 0
for i in range(1, s):
    if s % i == 0:
        result += i
    if result == n:
        print(n, s)

#var2

n = int(input('n = '))
m = int(input('m = '))
numbers_with_dividers = []
list_of_numbers = range(n, m + 1)
if n > 0 and n < m:
    for number in list_of_numbers:
        sum_of_dividers = 0
        for i in range(1, number // 2 + 1):
            if not number % i:
                sum_of_dividers += i
        if sum_of_dividers in list_of_numbers:
            numbers_with_dividers.append((number, sum_of_dividers))
result = []

for number, dividers in numbers_with_dividers:
    if (dividers, number) in numbers_with_dividers and dividers not in result:
        result.append(dividers)
print(result)
