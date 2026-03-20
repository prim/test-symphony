import unittest

from divide import divide


class DivideTests(unittest.TestCase):
    def test_divide_returns_quotient(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_supports_float_results(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_raises_for_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
