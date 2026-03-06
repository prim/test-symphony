from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_ls(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "ls.py"), *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )


def test_lists_current_directory_without_hidden_entries(tmp_path: Path) -> None:
    (tmp_path / "alpha.txt").write_text("alpha", encoding="utf-8")
    (tmp_path / "beta.txt").write_text("beta", encoding="utf-8")
    (tmp_path / ".secret").write_text("secret", encoding="utf-8")

    result = run_ls(cwd=tmp_path)

    assert result.returncode == 0
    assert result.stdout.splitlines() == ["alpha.txt", "beta.txt"]
    assert result.stderr == ""


def test_all_flag_includes_hidden_entries(tmp_path: Path) -> None:
    (tmp_path / "visible.txt").write_text("visible", encoding="utf-8")
    (tmp_path / ".hidden.txt").write_text("hidden", encoding="utf-8")

    result = run_ls("-a", cwd=tmp_path)

    assert result.returncode == 0
    assert result.stdout.splitlines() == [".hidden.txt", "visible.txt"]
    assert result.stderr == ""


def test_lists_multiple_targets_with_directory_headers(tmp_path: Path) -> None:
    target_dir = tmp_path / "docs"
    target_dir.mkdir()
    (target_dir / "guide.md").write_text("guide", encoding="utf-8")
    target_file = tmp_path / "README.txt"
    target_file.write_text("readme", encoding="utf-8")

    result = run_ls(str(target_file), str(target_dir), cwd=tmp_path)

    assert result.returncode == 0
    assert result.stdout == f"{target_file}\n\n{target_dir}:\nguide.md\n"
    assert result.stderr == ""


def test_empty_directory_produces_no_output(tmp_path: Path) -> None:
    result = run_ls(cwd=tmp_path)

    assert result.returncode == 0
    assert result.stdout == ""
    assert result.stderr == ""


def test_missing_path_returns_error(tmp_path: Path) -> None:
    result = run_ls("missing.txt", cwd=tmp_path)

    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr == "ls.py: cannot access 'missing.txt': No such file or directory\n"
