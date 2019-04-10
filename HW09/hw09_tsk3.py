'''
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.
'''

def even_nums(func):
    def wrapper (*args, **kwargs):
        new_args = [elem for i, elem in enumerate(*args) if i % 2 != 0]
        return func(new_args, **kwargs)
    return wrapper

@even_nums
def print_list(lst: list):
   print(lst)


lst = [1, 2, 3, 4]
print_list(lst)
