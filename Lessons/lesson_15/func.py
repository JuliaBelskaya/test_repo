def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if not y:
        raise ZeroDivisionError('AAAA')
    return x / y
