"""
41. Write a Python program to check whether a file exists
"""
import os.path

def check_file(file):
    """
    Checks wether or not a file exists in the current directory.

    Args:
    file = The name of the file to be verified
    Returns:
    True if file exists, false if not
    """
    return os.path.isfile(file)

print(check_file('w3_exercicio01.py'))
print(check_file('main.txt'))
