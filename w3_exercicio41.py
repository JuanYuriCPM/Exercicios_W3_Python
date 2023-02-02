"""
41. Write a Python program to check whether a file exists
"""
import os.path

def check_file(file):
    return os.path.isfile(file)

print(check_file('w3_exercicio01.py'))
print(check_file('main.txt'))
