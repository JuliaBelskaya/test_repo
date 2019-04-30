import scr.calc_functions.ui_func as ui
from scr.calc_functions.exceptions import (
                ZeroDivisionError,
                WrongTypeOfOperandsError,
                WrongTypeOfOperatorsError,
                IncorrectQuantityOfElementsError,
                NegativeOperatorsError,

)


def main():

    # ui.ui()

    try:
        ui.ui()
    except ZeroDivisionError as err:
        print(err)
    except WrongTypeOfOperandsError as err:
        print(err)
    except WrongTypeOfOperatorsError as err:
        print(err)
    except IncorrectQuantityOfElementsError as err:
        print(err)
    except NegativeOperatorsError as err:
        print(err)

if __name__ == "__main__":
    main()

