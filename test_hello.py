import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class HelloScriptTest(unittest.TestCase):
    def test_outputs_expected_text(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "hello.py")],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.stdout, "Hello Symphony\n")
        self.assertEqual(completed.stderr, "")


if __name__ == "__main__":
    unittest.main()
