# Написать игру. Пользователь должен угадать число. 
# Сперва вводиться диапазон угадывания. После колличество попыток. 
# В случае правильного ответа - выводить You are the winner. 
# В случае неправильного давать игроку подсказку(больше или меньше искомое число). 
# Если за указанное количество попыток число не угадано - выводить: 
# You are the loser и правильное число. 

from random import random
n = round(random() * 100)
i = 1
print('Компьютер загадал число. Отгадайте его. У вас 10 попыток')
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print('You are the  winner!')
        break
    i += 1
else:
    print('You are the looser. The right number is', n)

#var2
    
from random import randint

guess_from = int(input('guess from: '))
guess_to = int(input('guess to: '))
amount_of_try = int(input('amount of try: '))
rand_number = randint(guess_from, guess_to)

for i in range(amount_of_try):
    number = int(input('Guess the number: '))
    if number == rand_number:
        print('You are the winner')
        break
    elif number < rand_number:
        print('True number is bigger')
    else:
        print('True number is smaller')
else:
    print('You are the loser')    
