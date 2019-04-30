# В конец существующего текстового файла
# записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.[03-15.6]


with open('test.txt', 'a') as my_file:
    for i in range(3):
        new_line = input('enter new string --> ')
        my_file.write(f'\n{new_line}')