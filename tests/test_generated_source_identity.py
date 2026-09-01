#!/usr/bin/env python3
"""Make sure that setup and CMake use the generated boot-program stem."""

from pathlib import Path
import re
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]


def extract(path: Path, pattern: str, label: str) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(pattern, text)
    if not match:
        raise AssertionError(f"cannot find {label} in {path.relative_to(ROOT)}")
    return match.group(1)


def main() -> int:
    with (ROOT / "game.toml").open("rb") as stream:
        game = tomllib.load(stream)

    boot_exe = Path(game["prepare_disc"]["boot_exe"]).name
    expected_marker = f"generated/{boot_exe}_dispatch.c"
    expected_glob = f"generated/{boot_exe}_full_*.c"

    values = {
        "CMake marker": extract(
            ROOT / "CMakeLists.txt",
            r'\bGEN_MARKER\s+"([^"]+)"',
            "GEN_MARKER",
        ),
        "CMake full glob": extract(
            ROOT / "CMakeLists.txt",
            r'\bGEN_FULL_GLOB\s+"([^"]+)"',
            "GEN_FULL_GLOB",
        ),
        "setup marker": extract(
            ROOT / "codegen_setup.c",
            r'\.gen_marker_relpath\s*=\s*"([^"]+)"',
            "gen_marker_relpath",
        ),
    }

    expected = {
        "CMake marker": expected_marker,
        "CMake full glob": expected_glob,
        "setup marker": expected_marker,
    }
    problems = [
        f"{owner}: expected {expected[owner]}, found {value}"
        for owner, value in values.items()
        if value != expected[owner]
    ]
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        print("FAIL: generated source identity does not match game.toml", file=sys.stderr)
        return 1

    print(f"PASS: generated source identity is {boot_exe}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, OSError, AssertionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
