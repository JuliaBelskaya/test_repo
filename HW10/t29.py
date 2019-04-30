# Имеется текстовый файл. Все четные строки этого
# файла записать во второй файл, а нечетные —
# в третий файл. Порядок следования строк
# сохраняется.[03-15.29]

# with open('test.txt') as input_file, open('even.txt', 'w') as even_file, open('odd.txt', 'w') as odd_file:
with open('test.txt') as input_file:
    with open('even.txt', 'w') as even_file:
        with open('odd.txt', 'w') as odd_file:
            lines = input_file.readlines()
            for i, line in enumerate(lines):
                if i % 2:
                    odd_file.write(line)
                else:
                    even_file.write(line)