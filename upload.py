# coding: utf-8
import subprocess
import sys
subp = subprocess.Popen([sys.executable, "setup.py", "sdist", "bdist_wheel"])
subp.wait()
subp = subprocess.Popen([sys.executable, "-m", "twine", "upload", "dist/*"])
if subp.wait() == 1:
    subp = subprocess.Popen([sys.executable, "-m", "pip", "install", "twine"])
    subp.wait()
    subp = subprocess.Popen(
        [sys.executable, "-m", "twine", "upload", "dist/*"])
    subp.wait()
