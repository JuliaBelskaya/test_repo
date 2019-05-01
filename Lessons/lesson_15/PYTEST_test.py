# Покрыть тестами все функции через pytest


from .func import add, sub, div, mul


def test_add():
    result = add(1, 2)
    assert result == 3


def test_sub():
    result = sub(1, 2)
    assert result == -1


def test_div():
    result = div(2, 2)
    assert result == 1


def test_mul():
    result = mul(1, 2)
    assert result == 2
