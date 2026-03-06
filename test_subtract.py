import unittest

from subtract import subtract


class SubtractTest(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract(7, 0), 7)


if __name__ == "__main__":
    unittest.main()
