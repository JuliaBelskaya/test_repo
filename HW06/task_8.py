# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы. [02-7.2-HL08]

string = input ('-->') 
string = string.split(' ')
string = string[::-1]
print(string)

#var2

string = input('--> ')

words = string.split(' ')
new_string = ' '.join(words[::-1])
print(new_string)
