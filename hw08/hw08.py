#3
from math import sqrt


def func(x):
    return (sqrt(x) + x) / 2


x = func(5) + func(12) + func(19)
print(x)

# 7
def fact2(n: int):
    mult = 2 ** (1 - n % 2)

    # mult = 0
    # if n % 2 == 1:
    #     mult = 1
    # elif n % 2 == 0:
    #     mult = 2

    for i in range(mult, n + 1, 2):
        mult *= i
    return mult


print(fact2(9))
print(fact2(10))


# 9
from math import factorial as fact
from math import sin


def Sin1(x: float, e: float) -> float:
    sin_x = 0

    i = 0
    x_i = x  # (–1)^0 · x^(2·0+1) / (2·0 +1)! = x
    while x_i > e:
        sin_x += (-1) ** i * x_i
        i += 1
        x_i = x ** (2 * i + 1) / fact(2 * i + 1)

    return sin_x


x = 1
for i in range(3, 9):
    e = 10 ** -i
    print(f'{x} = x, e = {e}:\n\t{sin(x)}\n\t{Sin1(x, e)}\n')