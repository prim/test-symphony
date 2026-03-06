import unittest

from multiply import multiply


class MultiplyTests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_zero(self):
        self.assertEqual(multiply(0, 99), 0)

    def test_negative_number(self):
        self.assertEqual(multiply(-2, 5), -10)


if __name__ == "__main__":
    unittest.main()
