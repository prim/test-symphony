import unittest

from greet import farewell, greet


class GreetTestCase(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")


if __name__ == "__main__":
    unittest.main()
