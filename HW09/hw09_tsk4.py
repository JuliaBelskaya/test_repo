# Создать универсальны декоратор,
# который меняет порядок аргументов в функции на противоположный.

def reversed_args(func):
    def wrapper (*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


@reversed_args
def print_list(*args):
   print(args)


print_list(1, 2, 3, 4)


#var2

def backwards_args(func):
    def wrapper (*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


@backwards_args
def print_my_args(*args):
   print(args)


print_my_args(1, 2, 3, 4)
