'''
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.
'''

def even_nums(func):
    def wrapper (*args, **kwargs):
        new_args = [[x for x in arg if x % 2 != 0] for arg in args]
        return func(*new_args, **kwargs)
    return wrapper


@even_nums
def print_list(*args):
   print(args)


lst = [1, 2, 3, 4]
lst2 = list(range(5, 10))
print_list(lst, lst2)