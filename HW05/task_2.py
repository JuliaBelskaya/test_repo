# Для каждого натурального числа в промежутке 
# от m до n вывести все делители, кроме единицы 
# и самого числа. m и n вводятся с клавиатуры.

m, n = map(int, input().split())

for num in range(m, n+1):
    delimeters = []
    for del_1 in range(2, num):
        if num % del_1 == 0:
            delimeters.append(del_1)

    print(f'{num} {delimeters}')

#var2

n = int(input('n: '))
m = int(input('m: '))

for i in range(n, m + 1 ):
    row = []
    for j in range(2, i // 2 + 1):
        if not i % j:
            row.append(str(j))
    string = f'{i}: {" ".join(row)}'
    print(string)
