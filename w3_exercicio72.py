"""
72. Write a Python program to get the details of the math module
"""

import math

def get_details(command):
    return help(command)

print(get_details(math))
