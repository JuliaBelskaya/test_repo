from HW13.task02.classes import Book
from HW13.task02.exceptions import (

    WrongPagesTypeError,
    WrongPagesAmountError,
    WrongYearTypeError,
    FutureBookError,
    WrongAuthorTypeError,
    ZeroLengthAuthorError,
    WrongPriceTypeError,
    WrongPriceValueError,
)


def main():
    try:
        book = Book(-5, -5, -5, -5)
    except WrongPagesTypeError as err:
        print(err)
    except WrongPagesAmountError as err:
        print(err)
    except WrongYearTypeError as err:
        print(err)
    except FutureBookError as err:
        print(err)
    except WrongAuthorTypeError as err:
        print(err)
    except ZeroLengthAuthorError as err:
        print(err)
    except WrongPriceTypeError as err:
        print(err)
    except WrongPriceValueError as err:
        print(err)


if __name__ == '__main__':
    main()