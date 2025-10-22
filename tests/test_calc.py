from __future__ import annotations
import subprocess
import sys


def run_calc(*args: str) -> str:
out = subprocess.check_output([sys.executable, "-m", "calc", *args])
return out.decode().strip()


def test_add():
assert run_calc("add", "2", "3") == "5"
