import unittest

from add import add


class AddTests(unittest.TestCase):
    def test_add_positive_integers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_and_positive(self):
        self.assertEqual(add(-1, 5), 4)

    def test_add_floats(self):
        self.assertEqual(add(1.5, 2.5), 4.0)


if __name__ == "__main__":
    unittest.main()
