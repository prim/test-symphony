from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import ls


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "ls.py"


class ListPathTests(unittest.TestCase):
    def test_list_path_sorts_and_hides_dotfiles(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "beta.txt").write_text("beta", encoding="utf-8")
            (root / "alpha.txt").write_text("alpha", encoding="utf-8")
            (root / ".hidden").write_text("hidden", encoding="utf-8")

            self.assertEqual(ls.list_path(root), ["alpha.txt", "beta.txt"])

    def test_list_path_includes_dotfiles_with_flag(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "visible.txt").write_text("visible", encoding="utf-8")
            (root / ".hidden").write_text("hidden", encoding="utf-8")

            self.assertEqual(ls.list_path(root, include_hidden=True), [".hidden", "visible.txt"])


class CliTests(unittest.TestCase):
    def run_ls(self, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_lists_current_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "b.txt").write_text("b", encoding="utf-8")
            (root / "a.txt").write_text("a", encoding="utf-8")
            (root / ".hidden").write_text("hidden", encoding="utf-8")

            result = self.run_ls(cwd=root)

            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.splitlines(), ["a.txt", "b.txt"])
            self.assertEqual(result.stderr, "")

    def test_cli_supports_all_flag(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "visible.txt").write_text("visible", encoding="utf-8")
            (root / ".hidden").write_text("hidden", encoding="utf-8")

            result = self.run_ls("-a", cwd=root)

            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.splitlines(), [".hidden", "visible.txt"])

    def test_cli_lists_multiple_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            first = root / "first"
            second = root / "second"
            first.mkdir()
            second.mkdir()
            (first / "apple.txt").write_text("apple", encoding="utf-8")
            (second / "banana.txt").write_text("banana", encoding="utf-8")

            result = self.run_ls(str(first), str(second))

            self.assertEqual(result.returncode, 0)
            self.assertEqual(
                result.stdout.splitlines(),
                [str(first) + ":", "apple.txt", "", str(second) + ":", "banana.txt"],
            )

    def test_cli_lists_file_arguments_without_headers(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            nested = root / "nested"
            nested.mkdir()
            target = nested / "item.txt"
            target.write_text("content", encoding="utf-8")

            result = self.run_ls(str(target))

            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.splitlines(), [str(target)])
            self.assertEqual(result.stderr, "")

    def test_cli_lists_files_before_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "item.txt"
            folder = root / "folder"
            target.write_text("content", encoding="utf-8")
            folder.mkdir()
            (folder / "child.txt").write_text("child", encoding="utf-8")

            result = self.run_ls(str(target), str(folder))

            self.assertEqual(result.returncode, 0)
            self.assertEqual(
                result.stdout.splitlines(),
                [str(target), "", str(folder) + ":", "child.txt"],
            )

    def test_cli_reports_missing_path(self) -> None:
        result = self.run_ls("does-not-exist")

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("cannot access 'does-not-exist'", result.stderr)


if __name__ == "__main__":
    unittest.main()
