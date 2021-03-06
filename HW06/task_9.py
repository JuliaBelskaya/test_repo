# Создать список поездов. Структура словаря: 
# номер поезда, пункт и время прибытия, пункт и время отбытия. 
# Вывести все сведения о поездах, время пребывания в пути которых 
# превышает 7 часов 20 минут.[02-7.3-ML02]

trains = [
  {
        'number': '456987',
        'from': 'Minsk',
        'to': 'Warsaw',
        'departure': 7-00,
        'arrival': 8-00,
  },
  {
        'number': '456321',
        'from': 'Brest',
        'to': 'Moscow',
        'departure': 6-00,
        'arrival': 8-30,
  },
  {
        'number': '412397',
        'from': 'Kiyv',
        'to': 'Minsk',
        'departure': 14-00,
        'arrival': 23-30,
  },
]

        for key, value in trains.items():
            if 
            print(f'{key}: {value}')
        print('****')

#var2

from datetime import (
    timedelta, 
    datetime,
)

travel_time = timedelta(hours=7, minutes=20)
slow_trains = []
trains = [
    {
        'number': '1',
        'from': 'Kiev',
        'to': 'Minsk',
        'departure': datetime(2019, 3, 30, 19, 40),
        'arrival': datetime(2019, 3, 31, 5, 40),  
    },
    {
        'number': '2',
        'from': 'Minsk',
        'to': 'Moscow',
        'departure': datetime(2019, 3, 30, 23, 40),
        'arrival': datetime(2019, 3, 31, 10, 40),  
    },
    {
        'number': '3',
        'from': 'Minsk',
        'to': 'Vilnus',
        'departure': datetime(2019, 3, 30, 23, 40),
        'arrival': datetime(2019, 3, 31, 3, 40),  
    },
]

for train in trains:
    if train['arrival'] - train['departure'] > travel_time:
        slow_trains.append(train)

for train in slow_trains:
    for key, value in train.items():
        print(f'{key} --> {value}')
    print('-'*10)
