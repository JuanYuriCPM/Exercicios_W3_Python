"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

def check_number(n):
    if abs(1000 - n) <= 100 or abs(2000 - n) <= 100:
        return True
    else:
        return False

print(check_number(1899))