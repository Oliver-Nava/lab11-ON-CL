# https://github.com/Oliver-Nava/lab11-ON-CL
# Oliver Nava Partner 1
# Carlos Laege Partner 2
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(7, 2), 3.5)
        self.assertEqual(div(5, 10), 0.5)

    def test_multiply(self):
        self.assertEqual(mul(10, 0), 0)
        self.assertEqual(mul(7, 2), 14)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0, 10)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 1, 8)

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
