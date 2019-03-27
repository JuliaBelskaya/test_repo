#task_2

m, n = map(int, input().split())

for num in range(m, n+1):
    delimeters = []
    for del_1 in range(2, num):
        if num % del_1 == 0:
            delimeters.append(del_1)

    print(f'{num} {delimeters}')

