animal_list = ['cat', 'dog']
for animal in animal_list:
    print(animal)

a_list = [23, 42]
for elem in a_list:
    print(elem)

    
# Создать список с фамилиями. Вывести все фамилии, 
# которые начинаются на П и заканчиваются на а

lastnames = ['Петрова', 'Иванов', 'Пирова']

for lastname in lastnames:
    if lastname[0] == 'П' and lastname[-1] == 'а':
        print(lastname)

# Создать список учеников подобной структуры. 
# Определить средний балл оценок по всем предметам, 
# и вывести сведения о студентах, средний балл которых больше 4. [02-7.3-BL-02]

pupils = [
  {
        'firstname': 'Masha',
        'group': 'Ivanova',
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
  {
        'firstname': 'Natasha',
        'group': 'Petrova',
        'physics': 9,
        'informatics': 7,
        'history': 6,
  },
  {
        'firstname': 'Victor',
        'group': 'Ivanov',
        'physics': 2,
        'informatics': 4,
        'history': 3,
  },
]

for pupil in pupils:
    average = (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3
    if average > 4:

        for key, value in pupil.items():
            print(f'{key}: {value}')
        print('****')
