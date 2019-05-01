class ZeroDivisionError(ArithmeticError):
    def __init__(self, message="Происходит деление на ноль"):
        super().__init__(message)


class WrongTypeOfOperandsError(Exception):
    def __init__(self, message="Должно быть введено число. Тип int."):
        super().__init__(message)


class WrongTypeOfOperatorsError(Exception):
    def __init__(self, message="Должен быть введен арифметический знак"):
        super().__init__(message)


class IncorrectQuantityOfElementsError(Exception):
    def __init__(self, message="Введите два числа"):
        super().__init__(message)


class NegativeOperatorsError(Exception):
    def __init__(self, message="Число не может быть отрицательным"):
        super().__init__(message)


def validate_operands(x, y):
    if not isinstance(x, y, int):
        raise WrongTypeOfOperandsError
    elif x < 1 and y < 1:
        raise NegativeOperatorsError
    elif len(x) + len(y) > 2:
        raise IncorrectQuantityOfElementsError
