import scr.calc_functions.func as calc


def ui():
    operations_mapping = {
        "+": calc.add,
        "-": calc.sub,
        "*": calc.mul,
        "/": calc.div,
    }

    while True:
        operation = input('Enter +-*/: ')
        x, y = [int(n) for n in input('Enter x and y: ').split()]

        func = operations_mapping[operation]
        try:
            print(func(x, y))
        except ZeroDivisionError as e:
            print(e)

