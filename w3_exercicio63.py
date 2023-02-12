"""
63. Write a Python program to get an absolute file path.
"""

from pathlib import Path

path = Path('Buscando.pdf').parent.absolute()

print(path)
