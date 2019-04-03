x = int(input('Введите число '))
y = int(input('Введите число '))
sign = input('Введите знак операции ')
while True:
    if sign == '0':
        break
    if sign == '+':
        z = x + y
        print(f'{x} + {y} = {z}')
        continue
    elif sign == '-':
        z = x - y
        print(f'{x} - {y} = {z}')
        continue
    elif sign == '*':
        z = x * y
        print(f'{x} * {y} = {z}')
        continue
    elif sign == '/':
        if y != 0:
            z = x / y
            print(f'{x} / {y} = {z}')
        else:
            print('Деление на ноль, попробуйте еще раз')
        continue
    else:
        print('Неверный знак в операции')
        continue
