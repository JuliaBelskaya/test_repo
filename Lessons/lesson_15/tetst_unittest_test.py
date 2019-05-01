import unittest
from .func import add, sub, div, mul


class CalcTest(unittest.TestCase):
    def test_calc_sum(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_calc_sub(self):
        result = sub(2, 2)
        self.assertEqual(result, 0)

    def test_calc_div(self):
        result = div(2, 2)
        self.assertEqual(result, 1)

    def test_calc_mul(self):
        result = mul(2, 2)
        self.assertEqual(result, 4)

    def test_calc_div_exception(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


if __name__ == '__main__':
    unittest.main()
