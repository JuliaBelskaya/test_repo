# Покрыть тестами все функции


from .func import (
                add,
                sub,
                div,
                mul,

)


def test_add():
    result = add(1, 2)
    if result == 3:
        print('Test add(x, y) is OK')
    else:
        print('Test add(x, y) is Fail')


def test_sub():
    result = sub(2, 1)
    if result == 1:
        print('Test add(x, y) is OK')
    else:
        print('Test add(x, y) is Fail')


def test_div():
    result = div(2, 2)
    if result == 1:
        print('Test add(x, y) is OK')
    else:
        print('Test add(x, y) is Fail')


def test_mul():
    result = mul(2, 2)
    if result == 4:
        print('Test add(x, y) is OK')
    else:
        print('Test add(x, y) is Fail')


if __name__ == '__main__':
    test_add()
    test_sub()
    test_div()
    test_mul()
