import unittest
from .utils import Math


class CalcTest(unittest.TestCase):

    def setUp(self):
        self.math = Math(16, 4)
        self.math_div_exc = Math(16, 0)

    def test_calc_sum(self):
        result = self.math.calc_sum()
        self.assertEqual(result, 20)

    def test_calc_div(self):
        result = self.math.calc_div()
        self.assertEqual(result, 4)

    def test_calc_div_exc(self):
        with self.assertRaises(ZeroDivisionError):
            self.math_div_exc.calc_div()


if __name__ == '__main__':
    unittest.main()
