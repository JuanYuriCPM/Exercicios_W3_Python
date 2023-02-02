"""
20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""

def multiply_string(string, n):
    return string * abs(int(n))

print(multiply_string('batata', 3))