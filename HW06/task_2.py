# Дано число. Найти сумму и произведение его цифр.

n = input('Введите двухзначное число ')
mult = 1
summa = 0
for i in n:
    summa += int(i)
    if int(i) != 0:
        mult *= int(i)

print('Сумма цифр:', summa)
print('Произведение цифр:', mult)


#var2

summ = 0
multi = 1
number = input('number: ')
if number.isdigit():
    for digit in number:
        int_digit = int(digit)
        summ += int_digit
        multi *= int_digit
print(f'sum is {summ}')
print(f'multi is {multi}')
