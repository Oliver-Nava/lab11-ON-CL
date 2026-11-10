import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculator.div, 0, 10)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(2, 8), 3.0)

    def test_invalid_base(self):
        self.assertRaises(ValueError, calculator.logarithm, 1, 8)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
