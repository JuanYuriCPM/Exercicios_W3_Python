"""
16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""

def difference_from_17(n):
    if 17 >= n:
        return 17 - n
    else:
        return abs((17-n)*2)

print(difference_from_17(19))