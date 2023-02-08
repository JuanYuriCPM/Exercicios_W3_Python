"""
60. Write a Python program to calculate the hypotenuse of a right angled triangle.
"""

import math

def hypotenuse_calc(a, b):
    """
    Calculates the value of the hypotenuse of a right angled triangle

    Args:
    a: side a of the triangle
    b: side b of the triangle

    Returns:
    The value of the hypotenuse, according to the formula
    """
    return math.sqrt(a**2 + b**2)

print(hypotenuse_calc(3, 4))