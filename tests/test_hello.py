import subprocess
import sys
import unittest


class HelloScriptTest(unittest.TestCase):
    def test_hello_output(self):
        output = subprocess.check_output([sys.executable, "hello.py"])
        self.assertEqual(output.decode("utf-8"), "Hello from OpenCode!\n")


if __name__ == "__main__":
    unittest.main()
